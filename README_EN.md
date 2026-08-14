# Deconstructed Duotone Poster

[中文说明](README.md)

This is an image-styling skill for ChatGPT and Codex. It finds the main subjects in an image, breaks them into simple flat shapes, and turns them into a soft duotone editorial print with paper texture and film grain.

![City crossing example](examples/city-crossing.png)

## What it can do

- Turn a photo into a portrait 3:4 nine-square poster.
- Turn a wide photo into a landscape 4:3 six-square poster.
- Create a poster from a text theme without a source image.
- Add a requested subject to a source image.
- Keep a fixed pale ivory paper color and use one ink color chosen by the user.
- Add two small footer lines and simple icons based on the main subjects.

The cells do not repeat the same picture. The skill selects useful shapes, movements, materials, and small visual cues, then gives each cell a different flat interpretation. The result should feel like a printed poster, not a photo filter.

## Layouts

| Layout | Canvas | Grid | Best for |
| --- | --- | --- | --- |
| Nine-square | Portrait 3:4 | 3×3 squares | Portrait photos, square photos, and text themes |
| Six-square | Landscape 4:3 | 3×2 squares | Wide photos and landscape scenes |

Both layouts keep generous empty space. The top, left, and right paper margins are equal, and every cell is a true square. The landscape layout uses a smaller grid and wider outer margins.

## Visual style

- Large flat shapes instead of copied photo detail.
- Balanced detail without colored-pencil, sketch, or realistic rendering.
- Pale ivory paper with one user-selected ink color.
- Slight hand-printed softness around the shapes.
- Clear, strong glow while the main shapes stay readable.
- Natural paper texture and fine grain.
- Only two small footer lines and one to five subject icons.

## Install

Download or clone this repository, then install the complete `deconstructed-duotone-poster` folder as a custom skill. Do not copy only `SKILL.md`; the layout guides and rule files are also required.

For a local Codex setup:

```bash
git clone https://github.com/Lixorn/deconstructed-duotone-poster.git
mkdir -p ~/.codex/skills
cp -R deconstructed-duotone-poster/deconstructed-duotone-poster ~/.codex/skills/deconstructed-duotone-poster
```

## Use

Provide an image and an ink color:

```text
Use $deconstructed-duotone-poster to stylize this photo in powder blue.
```

Ask for the landscape layout:

```text
Use $deconstructed-duotone-poster to turn this wide photo into a landscape 4:3 six-square poster in forest green.
```

Create directly from a theme:

```text
Use $deconstructed-duotone-poster to create a brick-red poster about roads, beaches, and the sea.
```

Add a new subject to a source image:

```text
Use $deconstructed-duotone-poster with this coast photo and add a convertible car. Use cobalt blue ink.
```

For a batch, assign one color to each image:

```text
Use $deconstructed-duotone-poster on these three photos in cyan, red, and violet.
```

## Main modes

| Mode | Input | Result |
| --- | --- | --- |
| Source image | One or more images | Finds the subjects and redesigns each image |
| Text theme | A short text theme | Creates a new poster without a source image |
| Source plus subject | A source image and a requested subject | Keeps the source idea and introduces the new subject |

Ask for “Prompt only” if you only want the final generation prompt. Ask for analysis only if you want an explanation without making an image.

## Color

You can use a simple color name such as powder blue, brick red, forest green, or violet. You can also provide a hex value. The paper color stays at a light pale ivory: `#F7F1E3`.

The normal style uses pale ivory plus one ink color. If you clearly ask for multiple colors, the skill can use a small controlled palette based on the subjects, such as keeping different food colors in a food poster.

## Files

```text
.
├── README.md
├── README_EN.md
├── LICENSE
├── examples/
└── deconstructed-duotone-poster/
    ├── SKILL.md
    ├── agents/
    ├── assets/
    └── references/
```

## License

Released under the [MIT License](LICENSE).

