# Ninefold Duotone Grid

A custom ChatGPT/Codex skill that turns a photograph, a text-only theme, or a source image plus an added subject into a spacious duotone editorial print with portrait and landscape layouts.

![City crossing example](examples/city-crossing.png)

## What it does

- Reinterprets a source through nine portrait studies or six landscape studies.
- Supports a portrait 3:4 canvas with a 3×3 square grid and a landscape 4:3 canvas with a 3×2 square grid.
- Keeps the top, left, and right paper margins visually equal.
- Uses one pale ivory paper color and one user-selected ink color.
- Combines flat graphic cores, restrained printed edges, separate luminous halation, paper texture, and fine film grain.
- Adds exactly two small English typewriter lines and one to five semantic subject icons in the footer.
- Supports source-image transformation, text-only composition, and source plus added subject.

The included portrait and landscape structural guides are used only as image-generation references. They help the model preserve square cells and equal margins without programmatically cropping or compositing the finished artwork. The final print still receives organic inward dry-brush edges.

## Install

Download or clone this repository, then install the complete `ninefold-duotone-grid` folder as a custom skill in a client that supports ChatGPT/Codex skills.

For a local Codex setup:

```bash
git clone https://github.com/Lixorn/ninefold-duotone-grid.git
mkdir -p ~/.codex/skills
cp -R ninefold-duotone-grid/ninefold-duotone-grid ~/.codex/skills/ninefold-duotone-grid
```

Keep `SKILL.md`, `agents`, `assets`, and `references` together. Both layout guides in `assets` are required for automatic portrait/landscape routing.

## Use

Invoke the skill and provide one ink color.

```text
Use $ninefold-duotone-grid to stylize this photo in powder blue.
```

```text
Use $ninefold-duotone-grid to stylize this wide photo as a landscape 4:3 six-grid print in forest green.
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
| Source Transform | One or more source images | Nine portrait or six landscape reinterpretations derived from a small cue set |
| Theme Compose | Text only | A new cell system based on concrete theme anchors |
| Source + Added Subject | Source image plus a described or referenced subject | Source-led grid with a controlled subset reserved for the addition |
| Prompt-only | Any supported input | Plan, footer copy, cell matrix, and final generation prompt |
| Analyze-only | Existing work or a request for explanation | Visual-system analysis without generation |

## Visual contract

The portrait layout uses a 1200×1600 normalized canvas. Its 3×3 grid occupies `x=96..1104` and `y=96..1104`; all nine cells are 320×320 with 24-unit gutters and 96-unit top/side margins.

The landscape layout uses a 1600×1200 normalized canvas. Its 3×2 grid occupies `x=128..1472` and `y=128..1016`; all six cells are 432×432 with 24-unit gutters and 128-unit top/side margins. The fixed paper color in both layouts is `#F7F1E3`; the second designed color is selected by the user.

Square geometry is intentionally reinforced through written constraints and the matching `assets/layout-guide.png` or `assets/layout-guide-4x3.png`. Explicit ratio requests win; otherwise wide source images automatically use landscape 4:3, while portrait/square images and text-only themes use portrait 3:4. Image generation remains probabilistic, so the skill includes a quality gate and one targeted regeneration pass for visible failures.

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

`ninefold-duotone-grid` 会把照片或文字主题重新诠释为双色编辑海报。它支持 3:4 竖版九宫格和 4:3 横版六宫格，两种版式都使用严格方形的格子、相等的顶部与左右留白，并在下方保留两行极小英文打字机文字和与主体对应的极简图标。默认使用浅米白纸底，另一种墨色由使用者指定。

本仓库将可安装的 skill 单独放在 `ninefold-duotone-grid` 目录中，仓库根目录只承担配布说明与示例展示。结构母版只作为生图参考，不会对成品进行程序化裁切，也不会直接进入最终画面。

## License

MIT. See [LICENSE](LICENSE).
