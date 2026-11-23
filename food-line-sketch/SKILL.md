---
name: food-line-sketch
description: Turn a food or table photo into a naive, hand-drawn single-pen line illustration seen from above, like a ballpoint or fineliner doodle on plain paper. Redraw each dish, drink, utensil, and loose ingredient as a wobbly continuous outline with sparse decorative marks (rim dots, crumb specks, a soup spiral, seeds) and at most one tiny dense scribble accent, scattered with generous breathing room on a flat paper sheet. Use one line color and one background color; both are optional user choices with defaults of ballpoint blue `#2F62B3` on warm cream `#ECE5D1`. Use for food-photo transformations, dish-list prompts without a photo, batch conversions, prompt-only or analysis-only output, and exact color locking with the bundled recolor script.
---

# Food Line Sketch

Redraw a food photo as a calm, childlike-but-deliberate pen drawing: everything on the table becomes a loose top-down outline in one ink color on one paper color. Recognition comes from silhouette, a single characteristic interior mark, and arrangement, never from shading or color. Unless the user explicitly asks for analysis or prompt-only output, generate and return a raster image.

## Route the request

- Use **Photo Sketch** when one or more food, drink, or table photos are supplied. This is the default.
- Use **Dish List** when the user gives only words, such as "toast, olives, a lemon and a bowl of soup." Do not ask for a photo.
- Use **Prompt-only** only when explicitly requested. Return the plan and final prompt without claiming generation.
- Use **Analyze-only** only when asked to explain the style. Do not generate.
- For several unrelated photos, make one illustration per photo unless the user asks to combine them into one table.

## Load the references

- Read `references/request-modes.md` before resolving inputs, colors, and canvas.
- Read `references/line-language.md` for every request. It is the visual system.
- Read `references/object-vocabulary.md` before planning the objects.
- Read `references/prompt-compiler.md` for every generation or Prompt-only request.
- Read `references/quality-gate.md` before returning any image or prompt.

## Input contract

Colors are optional. Accept a color name or hex for the **line** and for the **background** independently. Missing line color defaults to ballpoint blue `#2F62B3`; missing background defaults to warm cream `#ECE5D1`. Normalize broad names with the table in `references/request-modes.md`, obey a supplied hex exactly, and state the resolved pair. Never ask for colors when the user did not mention them.

Check contrast before generating. If the pair's contrast ratio is below `3:1`, warn once and suggest a darker line or lighter background; proceed with the user's choice if they confirm or have already insisted.

Require either a usable photo or a dish list. Do not ask for anything else.

Always attach `assets/style-specimen.png` as a separate **line-style reference**. It shows stroke weight, wobble, overshoot, rim dots, speckle, spiral, and the single hatch accent. It is not a content source, layout, or color reference: its shapes must not be copied, and its colors are replaced by the resolved pair.

When the photo has a local path, pass the photo and `assets/style-specimen.png` to image generation with `referenced_image_paths`, labeling the photo as **semantic reference** and the specimen as **line-style reference**. When the photo exists only in recent conversation images, use `num_last_images_to_include` only if that mechanism can also include the specimen; otherwise ask the user to attach the photo again. Never mix both mechanisms. In Dish List mode attach only the specimen.

## Generation workflow

1. Route the request with `references/request-modes.md`. Resolve the line color, background color, and canvas ratio.
2. Inventory the photo: list every edible item, vessel, utensil, and loose ingredient. Keep three to nine primary objects. Drop hands, phones, packaging, menus, printed text, logos, tablecloth patterns, and background clutter.
3. For each kept object, choose its top-down outline and exactly one characteristic interior mark from `references/object-vocabulary.md`. Allow at most one or two small dense hatch/scribble accents in the whole picture.
4. Plan a loose flat-lay arrangement on the paper: keep the photo's rough left/right and near/far relations, but spread objects apart so most do not touch, leave generous empty paper, and let one hero dish sit slightly off-center and largest.
5. Compile one concrete prompt with `references/prompt-compiler.md`, then generate with the built-in image-generation tool.
6. Inspect with `references/quality-gate.md`. Regenerate once if any hard gate fails, putting the failed rule in the first two sentences of the revised prompt.
7. If the user asked for exact colors, or the result's ink or paper hue visibly drifts, and code execution is available, run `scripts/recolor.py` on the output with the resolved pair (see below) and return the recolored file.
8. Return the image first, then one compact note: mode, canvas, line color, background color, and the list of drawn objects with the mark chosen for each. Include the final prompt only when requested or useful for revision.

## Exact color locking

`scripts/recolor.py` maps any line drawing onto exactly two colors while keeping antialiasing and an optional faint paper texture:

```bash
python scripts/recolor.py input.png output.png --line "#2F62B3" --bg "#ECE5D1"
```

Options: `--texture 0..1` keeps that share of the source paper's tonal unevenness (default `0.35`; `0` gives perfectly flat paper); `--threshold` and `--softness` tune how faint marks are kept. Color names from the normalization table are accepted. Use it also when the user later asks for the same drawing in different colors: recolor instead of regenerating.

## Batch discipline

Keep the line color, background color, stroke weight, canvas ratio, and margin feel identical across a batch unless the user assigns colors per item. Make a fresh inventory and arrangement for every photo.

## Boundaries

- Do not trace, posterize, edge-detect, or filter the photo. Redraw from scratch.
- Do not shade, tone, model volume, cast shadows, or fill shapes with flat color. The only filled areas are tiny dense hatch accents.
- Do not use more than one line color or vary stroke weight beyond a single pen's natural pressure.
- Do not draw a table edge, tablecloth, background scene, frame, border, or perspective floor.
- Do not add text, labels, signatures, logos, or watermarks unless the user explicitly asks for a caption.
- Do not invent foods, garnishes, or utensils that are not in the photo or dish list.
- Do not let the drawing become polished vector art, a coloring-book page, a botanical illustration, or a cartoon with faces.

## Examples

- "Use $food-line-sketch on this brunch photo."
- "Use $food-line-sketch on this ramen photo, red line on pale pink paper."
- "把这张晚餐照片画成手绘线稿，线条用墨绿色，背景用 #F4EFE6。"
- "Use $food-line-sketch for toast, a soft-boiled egg, coffee and an orange — no photo."
- "Same drawing, but in black on white." (recolor with the script)
- "Prompt only for this picnic photo."
