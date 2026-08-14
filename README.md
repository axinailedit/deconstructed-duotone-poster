# Ninefold Duotone Grid

A custom ChatGPT/Codex skill that turns a photograph, a text-only theme, or a source image plus an added subject into a spacious portrait duotone editorial print.

![City crossing example](examples/city-crossing.png)

## What it does

- Reinterprets a source through nine related but distinct visual studies.
- Uses a portrait 3:4 canvas with a compact square 3×3 print block.
- Keeps the top, left, and right paper margins visually equal.
- Uses one pale ivory paper color and one user-selected ink color.
- Combines flat graphic cores, restrained printed edges, separate luminous halation, paper texture, and fine film grain.
- Adds exactly two small English typewriter lines and one to five semantic subject icons in the footer.
- Supports source-image transformation, text-only composition, and source plus added subject.

The included structural guide is used only as an image-generation reference. It helps the model preserve square cells and equal margins without programmatically cropping or compositing the finished artwork. The final print still receives organic inward dry-brush edges.

## Install

Download or clone this repository, then install the complete `ninefold-duotone-grid` folder as a custom skill in a client that supports ChatGPT/Codex skills.

For a local Codex setup:

```bash
git clone https://github.com/Lixorn/ninefold-duotone-grid.git
mkdir -p ~/.codex/skills
cp -R ninefold-duotone-grid/ninefold-duotone-grid ~/.codex/skills/ninefold-duotone-grid
```

Keep `SKILL.md`, `agents`, `assets`, and `references` together. The layout guide in `assets` is required for the default portrait workflow.

## Use

Invoke the skill and provide one ink color.

```text
Use $ninefold-duotone-grid to stylize this photo in powder blue.
```

```text
Use $ninefold-duotone-grid to create a brick-red print about roads, beaches, and the sea.
```

```text
Use $ninefold-duotone-grid with this coast photo and add a yellow convertible; keep cobalt blue as the ink.
```

The built-in normalized palette includes cobalt blue, powder blue, vermilion, brick red, forest green, olive green, violet, and charcoal navy. An explicit hex value takes priority.

## Modes

| Mode | Input | Result |
| --- | --- | --- |
| Source Transform | One or more source images | Nine reinterpretations derived from a small cue set |
| Theme Compose | Text only | A new nine-cell system based on concrete theme anchors |
| Source + Added Subject | Source image plus a described or referenced subject | Source-led grid with two to four cells reserved for the addition |
| Prompt-only | Any supported input | Plan, footer copy, cell matrix, and final generation prompt |
| Analyze-only | Existing work or a request for explanation | Visual-system analysis without generation |

## Visual contract

The default layout uses a 1200×1600 normalized canvas. The square grid occupies `x=96..1104` and `y=96..1104`; its nine cells are 320×320 with 24-unit gutters. Top, left, and right margins are all 96 units. The fixed paper color is `#F7F1E3`; the second designed color is selected by the user.

The square geometry is intentionally reinforced through both written constraints and `assets/layout-guide.png`. Image generation remains probabilistic, so minor raster-level drift may still occur even when the result is visually square. The skill includes a quality gate and one targeted regeneration pass for visible failures.

## Repository structure

```text
.
├── README.md
├── LICENSE
├── examples/
│   └── city-crossing.png
└── ninefold-duotone-grid/
    ├── SKILL.md
    ├── agents/
    ├── assets/
    └── references/
```

## 中文说明

`ninefold-duotone-grid` 会把照片或文字主题重新诠释为一张 3:4 竖版双色编辑海报。上方是具有统一视觉语言的九宫格，下方是两行极小英文打字机文字和与主体对应的极简图标。默认使用浅米白纸底，另一种墨色由使用者指定。

本仓库将可安装的 skill 单独放在 `ninefold-duotone-grid` 目录中，仓库根目录只承担配布说明与示例展示。结构母版只作为生图参考，不会对成品进行程序化裁切，也不会直接进入最终画面。

## License

MIT. See [LICENSE](LICENSE).
