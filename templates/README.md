# Workshop presentation template

`astar-template.pptx` is the original masterbrand deck with A*STAR-related images removed (16:9, 13.333" × 7.5", Open Sans) prepared for the `pptx` skill's template-editing workflow. Copy it, then unpack, duplicate, delete and edit slides as that skill describes. Do not edit the template in place. [astar-template-slides.jpg](astar-template-slides.jpg) shows all ten example slides, so you do not need to render the template yourself.

Every slide layout carries the "Simulation: ocelliq.com/astar-lr" notice: 11pt white text on an oxblood (`6D1A1F`) tab in the top-right corner. It is part of the layout, so it does not appear in `markitdown` output or slide XML; slides made from these layouts show it automatically. Do not cover it.

## Example slides

Each example slide's text placeholders contain the layout's style guidance (for example "Paragraph: Open Sans, regular 20pt, left align, maximum 170 words"). Replace all of that text, keeping each run's existing formatting. Delete any placeholder you do not use, and check with `markitdown` that no "Open Sans" guidance text, "Lorem ipsum" or "Content 1" remains. Placeholders `idx="63"` (security classification) and `idx="65"` (source/reference) are empty footers; fill `65` when a slide cites a source.

| Slide | Layout | Use for | Text slots |
| --- | --- | --- | --- |
| 1 | Cover 4 | Title slide; add a replacement photo if needed | `ctrTitle` title; `idx 67` subtitle; `idx 69` presenter, department, date |
| 2 | Divider 1A | Section divider | `ctrTitle` heading; `idx 67` subtitle. `idx 10` overlaps `idx 67`; fill one and delete the other |
| 3 | Content 1: Paragraph | Text up to 170 words | `idx 64` slide title; `idx 36` body |
| 4 | Content 3: Image with Text | Picture plus up to 50 words | `idx 75` slide title; `pic idx 17` image (left); `idx 66` body (right) |
| 5 | Content 6C: Big Idea | One message on a blue panel, with a visual on the right | `ctrTitle` message; `idx 10` up to 30 words; `idx 64` is the blue panel (keep its non-breaking space). The progress bars are ordinary shapes: edit or delete them |
| 6 | Figures: Key Data | Up to three headline numbers | `idx 75` slide title; `ctrTitle`, `idx 64`, `idx 66` numbers; `idx 54`, `idx 55`, `idx 56` captions |
| 7 | Content 6: Empty | Native, editable chart | `idx 75` slide title; the bar chart is `ppt/charts/chart1.xml` with its workbook in `ppt/embeddings/` |
| 8 | Content 6: Empty | Six-step process | `idx 75` slide title; six grouped text boxes joined by arrows |
| 9 | Content 6: Empty | Three titled lists | `idx 75` slide title; each group has a navy title box and a list box (bullets, numbers, ticks) |
| 10 | Closing 1 | Thank-you slide | `idx 64` contact line |

For a chart, edit slide 7's chart: change the series names and values in `chart1.xml` (the `c:strCache` and `c:numCache` entries) and the matching cells in the embedded workbook, or change the chart type there. Duplicates of slide 7 share the same chart part, so make only one chart this way, or add further charts as PNG images on a Content 6: Empty slide.

## Other layouts

Duplicate a layout with `add_slide.py unpacked/ slideLayoutN.xml` when no example slide fits. The new slide's placeholders are empty, so add a `<p:txBody>` with your text to each one you use.

| File | Name | Use for |
| --- | --- | --- |
| `slideLayout1`–`8` | Cover 1–8 | Alternative title slides; 1 and 6 take a picture (`pic idx 17` / `idx 70`) |
| `slideLayout9`–`12` | Divider 1A, 1B, 2A, 2B | Section dividers; B variants are centred |
| `slideLayout13` | Table of Content | Up to 12 numbered sections with page numbers |
| `slideLayout15` | Content 2: Image | Title plus one large picture |
| `slideLayout17` | Content 4: Table | Title plus a table (`tbl idx 66`) |
| `slideLayout18` | Content 5: Image Chart | Picture plus four short points (up to 15 words each) |
| `slideLayout19` | Content 6: Empty | Title only, for your own shapes |
| `slideLayout20`, `21` | Content 6A, 6B: Big Idea | Large picture with a headline message |
| `slideLayout24`, `25` | 2 or 3 Columns (Icons) | Side-by-side points with an icon, subject and paragraph each |
| `slideLayout26`, `27` | Profile: Individual, Team | People and contact details |
| `slideLayout28` | Contact Us | Up to three contacts |
| `slideLayout30` | Closing 2 | Alternative thank-you slide |

The theme colours are navy `003087` (accent 1), red `DA291C` (accent 2), orange `FF6720` (accent 3) and purple `5C068C` (accent 4); slide 7 uses them in that order. Prefer theme colours over new ones.

The public copy retains generic photos, graphics, editable charts and all ten example slides. Haiku identified seven embedded A*STAR-related images (logo variants and a branded building photo), which were removed from slides, layouts and the master; the branded cached thumbnail was also removed. The simulation notice, colours and layout geometry are retained.
