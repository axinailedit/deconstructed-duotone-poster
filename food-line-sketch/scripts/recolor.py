#!/usr/bin/env python3
"""Lock a line drawing to exactly one line color and one background color.

Estimates the paper locally (so uneven lighting in a photographed sheet is
removed), measures how far each pixel is from the paper toward the ink, and
re-composites that coverage with the requested colors. Antialiasing is kept,
and an optional share of the original paper unevenness can be retained.

Usage:
    python recolor.py input.png output.png --line "#2F62B3" --bg "#ECE5D1"

Requires Pillow and NumPy.
"""
import argparse
import sys

import numpy as np
from PIL import Image, ImageFilter

NAMES = {
    "ballpoint blue": "#2F62B3", "blue": "#2F62B3", "cobalt": "#2448A0",
    "navy": "#22305C", "ink blue": "#22305C", "black": "#1F1E1C", "ink": "#1F1E1C",
    "graphite": "#4A4A4A", "gray": "#4A4A4A", "grey": "#4A4A4A",
    "red": "#C2412D", "tomato": "#C2412D", "brick": "#9C3F2E",
    "vermilion": "#D9582B", "orange": "#D9582B", "forest green": "#2F5C43",
    "green": "#2F5C43", "olive": "#6B6E2F", "brown": "#6B4A32", "sepia": "#6B4A32",
    "violet": "#5B4A93", "purple": "#5B4A93",
    "warm cream": "#ECE5D1", "cream": "#ECE5D1", "ivory": "#F5F0E3",
    "paper white": "#FAF8F3", "white": "#FAF8F3", "oat": "#E3D8C1", "beige": "#E3D8C1",
    "pale pink": "#F3E0DA", "blush": "#F3E0DA", "butter": "#F4E9C4",
    "pale yellow": "#F4E9C4", "sage": "#DDE5D3", "pale green": "#DDE5D3",
    "sky": "#DCE6EE", "pale blue": "#DCE6EE", "lilac": "#E6DFEE", "kraft": "#CDB08A",
    "charcoal": "#2B2B2B",
}


def parse_color(value):
    v = value.strip().lower()
    v = NAMES.get(v, v)
    if v.startswith("#"):
        v = v[1:]
    if len(v) == 3:
        v = "".join(c * 2 for c in v)
    if len(v) != 6:
        raise argparse.ArgumentTypeError(f"not a hex color or known name: {value!r}")
    try:
        return np.array([int(v[i:i + 2], 16) for i in (0, 2, 4)], dtype=np.float32)
    except ValueError:
        raise argparse.ArgumentTypeError(f"not a hex color or known name: {value!r}")


def rel_luminance(rgb):
    c = rgb / 255.0
    c = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def contrast(a, b):
    la, lb = sorted((rel_luminance(a), rel_luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def estimate_paper(img):
    """Smooth per-pixel paper estimate that ignores thin strokes."""
    w, h = img.size
    scale = max(1, round(max(w, h) / 256))
    small = img.resize((max(1, w // scale), max(1, h // scale)), Image.BILINEAR)
    # Median/max removes thin dark lines; for light-on-dark drawings use min.
    arr = np.asarray(small, dtype=np.float32)
    lum = arr.mean(axis=2)
    dark_paper = np.median(lum) < 110
    k = 7
    small = small.filter(ImageFilter.MinFilter(k) if dark_paper else ImageFilter.MaxFilter(k))
    small = small.filter(ImageFilter.MedianFilter(k))
    small = small.filter(ImageFilter.GaussianBlur(6))
    return np.asarray(small.resize((w, h), Image.BILINEAR), dtype=np.float32)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input")
    ap.add_argument("output")
    ap.add_argument("--line", type=parse_color, default=parse_color("#2F62B3"), help="line color (hex or name)")
    ap.add_argument("--bg", type=parse_color, default=parse_color("#ECE5D1"), help="background color (hex or name)")
    ap.add_argument("--texture", type=float, default=0.35,
                    help="0..1 share of the source paper unevenness to keep (0 = perfectly flat)")
    ap.add_argument("--threshold", type=float, default=0.12,
                    help="0..1 coverage below which a pixel counts as paper (raise to drop faint noise)")
    ap.add_argument("--softness", type=float, default=0.55,
                    help="0..1 coverage range for the antialiased edge above the threshold")
    args = ap.parse_args()

    img = Image.open(args.input).convert("RGB")
    src = np.asarray(img, dtype=np.float32)
    paper = estimate_paper(img)

    diff = np.linalg.norm(src - paper, axis=2)
    ref = np.percentile(diff, 99.7)
    if ref < 8:
        sys.exit("no line work detected (image is almost uniform)")
    cov = diff / ref
    alpha = np.clip((cov - args.threshold) / max(args.softness, 1e-3), 0.0, 1.0)
    alpha = alpha * alpha * (3 - 2 * alpha)  # smoothstep keeps edges soft but cores solid

    bg = np.broadcast_to(args.bg, src.shape).astype(np.float32)
    t = float(np.clip(args.texture, 0.0, 1.0))
    if t > 0:
        plum = paper.mean(axis=2, keepdims=True)
        drift = (plum - np.median(plum)) / 255.0  # broad lighting drift
        fine = (src.mean(axis=2, keepdims=True) - plum) / 255.0 * (1 - alpha[..., None])
        bg = bg * (1 + t * (0.6 * drift + 0.8 * np.clip(fine, -0.04, 0.04)))

    out = bg * (1 - alpha[..., None]) + args.line * alpha[..., None]
    Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(args.output)

    c = contrast(args.line, args.bg)
    note = "" if c >= 3 else "  (warning: contrast below 3:1, thin lines may disappear)"
    print(f"saved {args.output}  line={'#%02X%02X%02X' % tuple(args.line.astype(int))} "
          f"bg={'#%02X%02X%02X' % tuple(args.bg.astype(int))} contrast={c:.1f}:1{note}")


if __name__ == "__main__":
    main()
