# Prompt compiler

Compile one concrete prompt in this order. Use visible nouns and verbs; do not rely on a style label alone.

## Paragraph 1: role of the inputs

- Photo Sketch: "The first attached image is a semantic reference only: use it to know which foods, vessels and utensils are on the table and roughly where. Do not trace it, keep its perspective, lighting, colors, or background."
- Dish List: "There is no source photo. The meal is: <items>."
- Always: "The attached style specimen shows only how the pen line behaves: stroke weight, wobble, overshoot, small dots, a spiral, and one tiny hatched patch. Do not copy its shapes or layout, and ignore its colors."

## Paragraph 2: medium and canvas

State the canvas ratio. Then: "A naive hand-drawn illustration made with a single <line color name> ballpoint pen (`<line hex>`) on plain <background name> paper (`<background hex>`) that fills the entire canvas. Seen directly from above as a flat lay. Only outlines: thin, even, continuous, slightly wobbly lines; circles slightly imperfect with overlapping or open ends; soft corners; lines may cross through each other transparently."

## Paragraph 3: objects

List every planned object in a natural reading order (top-left to bottom-right), each in one short clause with outline, mark, relative size, and position:

`top center: a bowl drawn as two loose concentric circles, a loose spiral inside for the soup, a spoon resting diagonally across its rim;`
`center right: the largest object, a plate with a ring of small oval dots between rim and well, a whole fish laid diagonally across it so the rim shows through the fish;`

State the hatch accent explicitly: "The only filled area is a small cheese wedge densely hatched with tight diagonal pen strokes." If none is planned, say "No filled areas at all."

## Paragraph 4: composition

"Objects are scattered loosely with generous empty paper between them; most do not touch. The drawing occupies about 70% of the canvas, with wide margins and nothing cropped at the edges. The <hero> is largest and slightly off-center; utensils lie at a slight diagonal. Keep the rough arrangement of the photo but loosen it."

## Paragraph 5: palette and paper

"Exactly two colors: <line hex> for every line, dot and hatch; <background hex> for the paper. The paper may have a very faint, soft, uneven daylight tone and barely visible tooth, but it reads as one flat color. No border, no table, no shadows."

## Paragraph 6: exclusions

End with the negative block, plus "no text" unless a caption was requested (then give the exact caption, its position, and handwriting style).

## Negative block

`no photograph, no photo filter, no traced photo edges, no posterization, no color fills, no second ink color, no shading, no gradients, no cast shadows, no highlights, no watercolor, no marker, no crayon, no pencil texture, no charcoal, no thick bold outlines, no coloring-book style, no vector-perfect circles, no ruler-straight lines, no comic inking, no faces on food, no botanical detail, no 3D, no perspective table, no table edge, no tablecloth, no background scene, no border, no frame, no notebook lines, no stains, no tape, no hands, no phone, no packaging, no logos, no labels, no text, no watermark, no signature, no cropped objects at the canvas edge, no crowded layout, no invented foods`

## Revision prompts

When regenerating after a failed gate, open with the failed rule in plain words, for example: "Previous attempt failed: objects were shaded with gray tones. Use outlines only, no shading at all." Then repeat the full prompt.

## Recoloring instead of regenerating

If the drawing is good and only colors are wrong or the user asks for a different pair, do not regenerate. Run `scripts/recolor.py` with the resolved line and background colors.
