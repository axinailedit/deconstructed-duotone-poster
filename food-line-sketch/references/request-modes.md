# Request modes

## Photo Sketch

Inspect every supplied photo. Treat it as an inventory and a rough map, not as a picture to copy. Record:

- Every edible item, drink, vessel (plate, bowl, glass, cup, board, pan), and utensil.
- Loose ingredients sitting on the table (a lemon, garlic, herbs, crumbs, olives).
- The rough position of each object: left/right, near/far, and which object is the hero.

Keep three to nine primary objects. If the photo holds more, merge repeats (six identical cups become one or two) and keep the most characteristic items. Treat many small items in one vessel (olives in a dish, berries in a bowl) as one object with a repeated interior mark.

Remove hands, faces, phones, menus, receipts, packaging, labels, printed text, logos, napkin prints, tablecloth patterns, chairs, walls, and background clutter. Keep a napkin only if it is a clear shape on the table, drawn as a plain loose rectangle outline.

Convert every viewpoint to a top-down flat lay. A photo shot at an angle is re-imagined from above; plates and bowls become near-circles, boards become soft rectangles. Glasses and cups may keep a naive mixed viewpoint: a rim loop plus a visible base loop, as in a child's drawing.

## Dish List

Use this mode when no image is supplied. Parse the text into concrete dishes and items. Add a vessel only when the dish obviously needs one (soup needs a bowl, coffee needs a cup); do not add extra foods, garnishes, or utensils. Plan the arrangement from scratch with the same composition rules. Do not claim to have inspected a photo.

## Batch

For several photos, default to one illustration per photo, each with its own inventory. Combine them onto one table only when the user asks.

## Prompt-only and Analyze-only

Prompt-only returns the resolved colors, canvas, object plan, and final prompt plus the negative block. Analyze-only explains the line language, object vocabulary, and failure directions without generating.

## Canvas

- Obey an explicit ratio (`3:4`, `4:3`, `1:1`, `2:3`, `9:16`, portrait, landscape, square).
- With no explicit ratio, use landscape `4:3` when the photo's width is at least `1.15` times its height; otherwise use portrait `3:4`.
- Dish List defaults to portrait `3:4`.

## Colors

Two independent optional choices: **line** (ink) and **background** (paper).

Defaults:

- line: ballpoint blue `#2F62B3`
- background: warm cream `#ECE5D1`

Normalize broad names to one solid value and state it:

| Name | Hex | Name | Hex |
| --- | --- | --- | --- |
| ballpoint blue / blue | `#2F62B3` | warm cream / cream | `#ECE5D1` |
| cobalt | `#2448A0` | ivory | `#F5F0E3` |
| navy / ink blue | `#22305C` | paper white / white | `#FAF8F3` |
| black / ink | `#1F1E1C` | oat / beige | `#E3D8C1` |
| graphite / gray | `#4A4A4A` | pale pink / blush | `#F3E0DA` |
| red / tomato | `#C2412D` | butter / pale yellow | `#F4E9C4` |
| brick | `#9C3F2E` | sage / pale green | `#DDE5D3` |
| vermilion / orange | `#D9582B` | sky / pale blue | `#DCE6EE` |
| forest green / green | `#2F5C43` | lilac | `#E6DFEE` |
| olive | `#6B6E2F` | kraft | `#CDB08A` |
| brown / sepia | `#6B4A32` | charcoal (dark paper) | `#2B2B2B` |
| violet / purple | `#5B4A93` | navy (dark paper) | `#1E2740` |
| white (on dark paper) | `#F4F1EA` | | |

Any color may be used for either role; the table only resolves names. Obey supplied hex values exactly.

Compute the WCAG contrast ratio of the pair. Below `3:1`, warn once that thin lines may disappear and suggest a darker line or lighter paper. A light line on dark paper is allowed (chalk-on-slate feel); keep the same line language.

## Optional caption

Add text only when the user explicitly asks. Then place one short line of handwritten lowercase text in the line color, small, near the bottom-left margin, and preserve the user's wording verbatim.
