# Quality gate

Inspect the output at full size and at thumbnail size. Check structure before charm.

## Hard gates

Any failure here requires one regeneration (or a recolor for gates 2–3 when the drawing is otherwise good).

1. Canvas ratio matches the resolved ratio.
2. Exactly one line color, visibly matching the resolved line hex. No second ink, gray tone, or colored fill.
3. The background is one color matching the resolved background hex, with at most faint natural unevenness. No border, table, frame, or visible sheet edge.
4. Everything is outline drawing. No shading, gradients, shadows, highlights, or filled shapes except at most one or two small dense hatch accents (under about 1% of canvas).
5. Stroke weight is thin and consistent, like one pen. Reject bold coloring-book outlines, brush taper, and pencil or crayon texture.
6. Lines are hand-drawn: gentle wobble, imperfect circles, soft corners, occasional overshoot. Reject vector-perfect geometry and traced photo contours.
7. Every planned object is present and recognizable; nothing extra was invented. Hands, phones, packaging, text, and logos are absent.
8. Viewpoint is top-down flat lay (glasses may use naive mixed view). No perspective table, horizon, or vanishing point.
9. Composition: generous empty paper, nothing cropped by the canvas edge, most objects separated, one clear hero, no rigid grid.
10. No text anywhere unless a caption was requested; a requested caption matches the user's wording.

## Soft checks

- Each object carries exactly one characteristic mark family; repeated marks vary in size and spacing.
- At least one transparent overlap reads naturally (a utensil on a plate, a fish across a rim), if the plan included one.
- The drawing feels calm and sparse, closer to a diary sketch than an illustration plate.
- At thumbnail scale the line still reads; if it disappears, the contrast pair is too weak or the stroke too thin.

## Prompt-only audit

Verify the prompt states: input roles (semantic photo, line-style specimen), canvas ratio, line and background hex values, top-down flat lay, outline-only rule, every object with outline/mark/size/position, the hatch accent or "no filled areas", composition and margin rules, the two-color paper rule, and the negative block.

Do not present a second failed result as successful. Say what still fails and offer to recolor or adjust the plan.
