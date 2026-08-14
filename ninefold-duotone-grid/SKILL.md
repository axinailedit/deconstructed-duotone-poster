---
name: ninefold-duotone-grid
description: Transform a supplied image, a text-only theme, or a source image plus a requested added subject into a spacious portrait 3:4 editorial duotone print. Enforce the upper 3x3 grid with a fixed 1200x1600 design coordinate system, equal top/left/right paper margins, one shared exact-square tile template, and zero visible rectangular drift while retaining a faint inward hand-printed fringe. Use medium-flat interpretations, pale ivory paper, one user-chosen ink, stable flat fills with strong separate halation but restrained ink bleed, and a quiet lower footer with two very small English typewriter lines plus one ultra-minimal subject icon for a single subject or two to five icons for multiple subjects. Use for image transformations, theme-only prompts, adding a specified subject, prompt-only or analysis-only output, and batch variations in this visual family.
---

# Ninefold Duotone Grid

Extract a small set of useful visual ideas and reinterpret them nine ways. Let the grid as a whole carry recognition: most individual cells may be abstract, while a few preserve restrained signature cues. Favor broad filled masses, negative-space cuts, mark rhythms, and material behavior over illustrated objects. Unless the user explicitly requests analysis or prompt-only output, generate and return a raster image.

## Route the request

- Use **Source Transform** when one or more supplied images provide the subject or scene.
- Use **Theme Compose** when the user supplies only words or a concept, such as “公路、沙滩和大海.” Do not ask for an image.
- Use **Source + Added Subject** when the user supplies a source and asks to introduce another specified subject. Accept either a textual subject or an additional subject-reference image.
- Use **Prompt-only** only when explicitly requested. Return the mode, exact footer copy, nine-cell plan, and final prompt without claiming generation.
- Use **Analyze-only** only when asked to explain the visual system. Do not generate.
- For multiple unrelated source images, default to one finished print per image. Combine them only when requested.

## Load the references

- Read `references/request-modes.md` before resolving inputs and image roles.
- Read `references/visual-system.md` for every request.
- Read `references/interpretation-matrix.md` before planning the nine cells.
- Read `references/prompt-compiler.md` for every generation or Prompt-only request.
- Read `references/quality-gate.md` before returning any image or prompt.

## Input contract

Require one user-chosen hue in every generation mode. Accept a color name or hex value. Normalize a broad name to one representative solid color and state it. If color is missing, ask only for the color.

Require either a usable source image or a text theme. In Source + Added Subject mode, require the added subject as a short description or reference image. Ask for a reference only when exact identity, character design, or product geometry matters and cannot be inferred safely.

If the user supplies footer copy, preserve it verbatim and break it naturally into exactly two left-aligned lines unless the user explicitly requests one line. Otherwise synthesize one short ASCII-English description from the semantic anchors: target 3–7 words and 12–32 characters, then choose and preserve one exact two-line break. Do not copy visible source text, brands, dates, or locations.

For the default portrait `3:4` layout, always include `assets/layout-guide.png` as a separate **structural layout reference** in image generation. It is a guide, not an edit target, subject source, or style reference. Require the model to follow its square positions and margins while redrawing all pigment edges organically. Never expose the neutral guide color in the finished palette.

When every target image has a local path, pass those paths plus `assets/layout-guide.png` to image generation with `referenced_image_paths`. In Theme Compose, pass only the guide. When at least one semantic target exists only in recent conversation images, use `num_last_images_to_include` only if that mechanism can also include the guide; otherwise ask the user to attach the missing semantic image again so local paths can be used. Never use both image-input mechanisms. If neither includes every required image, ask the user to attach it again.

## Generation workflow

1. Route the request with `references/request-modes.md`. Label each image as source reference or added-subject reference.
2. Extract three to five semantic anchors. Select only two to four signature cues to preserve across the entire grid; discard incidental components, literal lighting, construction detail, and photographic microdetail.
3. Build nine medium-flat cells with `references/interpretation-matrix.md`. Give each cell one broad mass, void, gesture, or material rhythm plus at most one to three supporting mark families. Make four to six cells abstract or material-led, two to four semi-literal cue studies, and no more than one simplified scene fragment.
4. For Source + Added Subject mode, reserve two to four cells for the added subject or its relationship with source anchors. Do not paste the subject into all nine cells.
5. Choose the exact short English footer copy and its exact two-line break. Count the primary semantic subjects, then plan the footer icons with `references/visual-system.md`: exactly one icon for one subject; one icon per subject for multiple subjects, clamped to two through five.
6. Lock the palette to fixed pale ivory cream `#F7F1E3` plus the chosen solid ink. Use the default portrait `3:4` spacious exact-square-grid/quiet-footer layout and fixed coordinate system in `references/visual-system.md` unless the user explicitly overrides the ratio. Treat the grid as one locked square scaffold populated by nine copies of one shared square tile frame; never ask the image model to improvise nine separate frame shapes.
7. Compile one concrete prompt with `references/prompt-compiler.md`, then generate with the built-in image-generation tool. Attach the fixed structural guide for every default portrait `3:4` generation. Label all other images by their semantic roles and explicitly state that the guide contributes geometry only.
8. Inspect with `references/quality-gate.md`. Regenerate once if the default image is not portrait 3:4; the grid does not map to the fixed coordinates; the top, left, and right paper margins are not equal; any outer-grid or cell width/height differs by more than one output pixel after proportional scaling; the footer dominates; copy is not exactly two small left-aligned lines; subject-icon count or identity is wrong; cells become detailed illustrations or empty generic symbols; ink edges become cloudy or smeared; glow is weak; the paper is too dark; the palette gains a third hue; paper texture is absent; or footer text is unreadable.
9. Return the image, mode, palette, exact footer copy, and a concise nine-cell interpretation list. Include the final prompt only when requested or useful for revision.

## Batch discipline

Keep pale ivory cream, exact-square grid geometry, footer scale, flat-core/halo separation, and paper treatment identical across a batch. Keep the chosen hue identical unless the user assigns colors per item. Derive new anchors and nine-cell plans for every item. Derive footer icons from each item’s actual subjects; never add arbitrary decorative geometry.

## Boundaries

- Do not paste, trace, collage, posterize, or reconstruct the original image.
- Do not require every cell to identify the source alone. Preserve only a few signature cues across the grid; let the remaining cells translate motion, material, contour, reflection, erosion, rhythm, or negative space.
- Do not render detailed equipment assemblies, repeated architectural openings, brick-by-brick paving, line-art construction, complete foreground/midground/background scenes, photorealistic volume, literal lighting, or dense microdetail.
- Do not reduce every cell to one generic logo-like mark. Keep controlled secondary rhythms and varied densities so the grid remains visually rich.
- Do not use razor-sharp pictorial vectors, brittle straight corners, hard clipped silhouettes, or repeated stock geometry. Keep a stable flat core, then use only a narrow printed transition and a separate luminous halo; do not dissolve shapes into fuzzy ink clouds.
- Do not let the added subject crowd every cell or erase the source-derived system.
- Do not add text outside the footer or arbitrary geometry in the footer. Use only the planned subject-derived icon or icons.
- Do not let paper texture, grain, or glow introduce a designed third color or obscure the grid.
- Do not simulate paper with uniform noise. Require fibers, pressed-pulp mottling, and absorbed ink.

## Output forms

For generation, return the raster first and one compact note with mode, palette, footer copy, and nine interpretations. For Prompt-only, return the same plan followed by the final prompt and negative constraints. For Analyze-only, return fixed rules, mode variables, and failure directions.

## Examples

- “用 $ninefold-duotone-grid 把这张照片做成浅蓝色九格图。”
- “用 $ninefold-duotone-grid 做一张关于公路、沙滩和大海的砖红色图，不提供照片。”
- “用这张海岸照片，但额外加入一辆黄色敞篷车；主色仍用钴蓝。”
- “只给我最终 Prompt，底部英文写 ROAD, SAND AND SEA。”
