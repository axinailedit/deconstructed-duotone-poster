#!/usr/bin/env python3
"""Regenerate assets/style-specimen.png: abstract pen-line behavior samples.

The specimen shows stroke weight, wobble, overshoot, dot rings, speckle,
a spiral, transparent crossings, and one dense hatch accent. It deliberately
contains no complete food objects so image models borrow the line, not content.

Usage: python make_style_specimen.py [output.png]
"""
import math
import os
import sys

import numpy as np
from PIL import Image, ImageDraw

W, H, SS = 1200, 900, 4  # output size, supersampling
INK = (47, 98, 179)
PAPER = (236, 229, 209)
STROKE = 3.6  # px at output size
rng = np.random.default_rng(7)


def wobble(n, amp, freq=3):
    t = np.linspace(0, 1, n)
    out = np.zeros(n)
    for k in range(1, freq + 1):
        out += rng.normal(0, amp / k) * np.sin(2 * math.pi * k * t + rng.uniform(0, 6.28))
    return out


def loop(cx, cy, rx, ry, rot=0.0, overlap=0.08, amp=0.035):
    n = 220
    t = np.linspace(0, 2 * math.pi * (1 + overlap), n) + rng.uniform(0, 6.28)
    r = 1 + wobble(n, amp)
    x, y = rx * r * np.cos(t), ry * r * np.sin(t)
    c, s = math.cos(rot), math.sin(rot)
    return list(zip(cx + x * c - y * s, cy + x * s + y * c))


def line(p0, p1, amp=4.0, overshoot=0.04):
    n = 80
    t = np.linspace(-overshoot, 1 + overshoot, n)
    x = p0[0] + (p1[0] - p0[0]) * t
    y = p0[1] + (p1[1] - p0[1]) * t
    nx, ny = -(p1[1] - p0[1]), p1[0] - p0[0]
    L = math.hypot(nx, ny) or 1
    w = wobble(n, amp, 2)
    return list(zip(x + nx / L * w, y + ny / L * w))


def spiral(cx, cy, r, turns=2.3):
    n = 300
    t = np.linspace(0, 1, n)
    a = t * turns * 2 * math.pi
    rr = r * (0.12 + 0.88 * t) * (1 + wobble(n, 0.04))
    return list(zip(cx + rr * np.cos(a), cy + rr * np.sin(a)))


def main(out):
    img = Image.new("RGB", (W * SS, H * SS), PAPER)
    d = ImageDraw.Draw(img)
    width = round(STROKE * SS)

    def stroke(pts):
        d.line([(x * SS, y * SS) for x, y in pts], fill=INK, width=width, joint="curve")
        r = width / 2
        for x, y in (pts[0], pts[-1]):
            d.ellipse([x * SS - r, y * SS - r, x * SS + r, y * SS + r], fill=INK)

    def dot(x, y, r):
        d.ellipse([(x - r) * SS, (y - r) * SS, (x + r) * SS, (y + r) * SS], fill=INK)

    # 1. Double rim with a ring of small open ovals.
    cx, cy = 260, 250
    stroke(loop(cx, cy, 170, 160, overlap=0.05))
    stroke(loop(cx, cy, 118, 110, overlap=0.1))
    for i in range(22):
        a = 2 * math.pi * i / 22 + rng.normal(0, 0.04)
        r = 144 + rng.normal(0, 2.5)
        stroke(loop(cx + r * math.cos(a), cy + r * math.sin(a), 6.5, 4.2, rot=a, overlap=0.05, amp=0.06))

    # 2. Transparent crossing: a long loose spindle passing over the rim.
    stroke(line((140, 120), (420, 395), amp=5))
    stroke(line((150, 150), (400, 415), amp=5))

    # 3. Spiral inside a single loop.
    stroke(loop(640, 230, 120, 112, overlap=0.12))
    stroke(spiral(640, 232, 70))

    # 4. Speckle field inside an irregular outline.
    stroke(loop(990, 250, 140, 105, rot=0.3, overlap=0.04, amp=0.08))
    stroke(loop(990, 250, 118, 86, rot=0.3, overlap=0.06, amp=0.08))
    for _ in range(26):
        a, r = rng.uniform(0, 6.28), math.sqrt(rng.uniform(0, 1))
        dot(990 + 95 * r * math.cos(a), 250 + 66 * r * math.sin(a), rng.uniform(1.6, 2.6))

    # 5. Cluster of small open ovals with pit dots.
    for i in range(7):
        a = 2 * math.pi * i / 7 + rng.normal(0, 0.15)
        ox, oy = 250 + 62 * math.cos(a), 650 + 55 * math.sin(a)
        stroke(loop(ox, oy, 22, 30, rot=rng.uniform(0, 3), overlap=0.06, amp=0.05))
        dot(ox + rng.normal(0, 5), oy - 10, 2.2)
    stroke(loop(250, 650, 125, 118, overlap=0.07))

    # 6. Dense hatch accent: one small soft triangle filled with tight strokes.
    tri = [(560, 560), (700, 600), (585, 700)]
    for i in range(3):
        stroke(line(tri[i], tri[(i + 1) % 3], amp=2, overshoot=0.06))
    # Tight parallel diagonal hatching clipped to the triangle: lines x - 0.7*y = c.
    def edge_hits(c):
        hits = []
        for i in range(3):
            (x0, y0), (x1, y1) = tri[i], tri[(i + 1) % 3]
            f0, f1 = x0 - 0.7 * y0 - c, x1 - 0.7 * y1 - c
            if f0 * f1 < 0:
                s = f0 / (f0 - f1)
                hits.append((x0 + (x1 - x0) * s, y0 + (y1 - y0) * s))
        return hits
    vals = [x - 0.7 * y for x, y in tri]
    for c in np.arange(min(vals) + 3, max(vals) - 1, 5.2):
        hits = edge_hits(c)
        if len(hits) == 2:
            stroke(line(hits[0], hits[1], amp=0.8, overshoot=-0.03))

    # 7. Long gently bowed strokes with overshoot and a segment star.
    stroke(line((820, 520), (1110, 600), amp=6, overshoot=0.06))
    stroke(line((800, 560), (1080, 660), amp=6, overshoot=0.06))
    cx, cy = 950, 760
    stroke(loop(cx, cy, 62, 60, overlap=0.06))
    stroke(loop(cx, cy, 50, 48, overlap=0.06))
    for i in range(8):
        a = 2 * math.pi * i / 8 + 0.2
        stroke(line((cx, cy), (cx + 44 * math.cos(a), cy + 44 * math.sin(a)), amp=1.2, overshoot=0.0))

    img = img.resize((W, H), Image.LANCZOS)
    img.save(out)
    print("saved", out)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, "..", "assets", "style-specimen.png"))
