"""Build the seven-slide Code Nashai deck as editable PPTX, vector PDF and PNGs.

Requires python-pptx, reportlab and Pillow. No network or model calls.
Run from the repository root: python scripts/build-pitch-deck.py
"""
from pathlib import Path
import hashlib
import json
import math
import shutil

from PIL import Image, ImageDraw, ImageFont
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/presentation'
OUT.mkdir(parents=True, exist_ok=True)
W, H = 1600, 900
NAVY, INK, WHITE, MUTED = '#102A43', '#172F44', '#F8FAFC', '#AFC1CF'
BLUE, PALE, LINE, AMBER = '#2B6D91', '#E7F0F5', '#C6D4DF', '#F0BD65'
FONT_DIR = Path('C:/Windows/Fonts')
if not (FONT_DIR / 'arial.ttf').exists():
    FONT_DIR = Path('/usr/share/fonts/truetype/liberation2')
regular = FONT_DIR / ('arial.ttf' if (FONT_DIR / 'arial.ttf').exists() else 'LiberationSans-Regular.ttf')
bold = FONT_DIR / ('arialbd.ttf' if (FONT_DIR / 'arialbd.ttf').exists() else 'LiberationSans-Bold.ttf')
pdfmetrics.registerFont(TTFont('Deck', str(regular)))
pdfmetrics.registerFont(TTFont('DeckBold', str(bold)))
prs = Presentation()
prs.slide_width, prs.slide_height = Inches(16), Inches(9)
prs.core_properties.title = 'Flame Freefall | Code Nashai'
prs.core_properties.author = 'Muhammad Marjan Ahmed'
prs.core_properties.subject = 'NASA Space Apps challenge response: Flame in Freefall'
pdf = canvas.Canvas(str(OUT / 'flame-freefall-pitch.pdf'), pagesize=(W, H))
pdf.setTitle('Flame Freefall | Code Nashai | Seven-slide project demonstration')
pdf.setAuthor('Muhammad Marjan Ahmed')
slides, notes = [], []

def rgb(c):
    return tuple(int(c[i:i+2], 16) for i in (1, 3, 5))

def rect(x, y, w, h, color):
    draw.rectangle((x, y, x+w, y+h), fill=color)
    pdf.setFillColorRGB(*[v/255 for v in rgb(color)])
    pdf.rect(x, H-y-h, w, h, stroke=0, fill=1)
    s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x/100), Inches(y/100), Inches(w/100), Inches(h/100))
    s.fill.solid(); s.fill.fore_color.rgb = RGBColor(*rgb(color)); s.line.fill.background()

def text(x, y, content, size=30, color=INK, weight=False, width=1450, leading=1.18):
    font = ImageFont.truetype(str(bold if weight else regular), size)
    for i, line in enumerate(content.split('\n')):
        yy = y + i*size*leading
        draw.text((x, yy), line, font=font, fill=color)
        pdf.setFillColorRGB(*[v/255 for v in rgb(color)])
        pdf.setFont('DeckBold' if weight else 'Deck', size)
        pdf.drawString(x, H-yy-size*.94, line)
        assert pdfmetrics.stringWidth(line, 'DeckBold' if weight else 'Deck', size) <= width+8, (len(slides), line)
    box = slide.shapes.add_textbox(Inches(x/100), Inches(y/100), Inches(width/100), Inches((len(content.split('\n'))*size*leading+12)/100))
    tf = box.text_frame; tf.word_wrap = False
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    for i, line in enumerate(content.split('\n')):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = line; p.font.name = 'Arial'; p.font.size = Pt(size*.72)
        p.font.bold = weight; p.font.color.rgb = RGBColor(*rgb(color))
        p.space_before = p.space_after = Pt(0)
        p.line_spacing = 1.18

def begin(title, dark=False, source=''):
    global slide, im, draw, dark_slide
    dark_slide = dark
    slide = prs.slides.add_slide(prs.slide_layouts[6]); slides.append(title)
    im = Image.new('RGB', (W, H), NAVY if dark else WHITE); draw = ImageDraw.Draw(im)
    rect(0, 0, W, H, NAVY if dark else WHITE)
    text(72, 34, 'Code Nashai  /  Flame Freefall', 20, MUTED if dark else BLUE, True)
    if title:
        text(72, 107, title, 57, WHITE if dark else INK, True)
    rect(72, 818, 1456, 1, '#3C5367' if dark else LINE)
    text(72, 835, source, 15, MUTED if dark else '#50677B', width=1370)
    text(1456, 835, f'{len(slides)} / 7', 17, MUTED if dark else BLUE, width=90)

def end(note):
    slide.notes_slide.notes_text_frame.text = note
    notes.append(note)
    im.save(OUT / f'slide-{len(slides):02}.png')
    pdf.showPage()

def picture(file, x, y, w, h):
    pic = Image.open(file).convert('RGB')
    im.paste(pic.resize((int(w), int(h)), Image.Resampling.LANCZOS), (int(x), int(y)))
    pdf.drawImage(ImageReader(pic), x, H-y-h, w, h)
    slide.shapes.add_picture(str(file), Inches(x/100), Inches(y/100), Inches(w/100), Inches(h/100))

bundle_bytes = (ROOT / 'psi-data/derived/runs.json').read_bytes()
bundle = json.loads(bundle_bytes); runs = bundle['runs']; index = {r['id']: r for r in runs}
individual = sum(r.get('granularity') in ('test', 'test-point') for r in runs)
assert len(runs) == 1951 and individual == 1838
for rid, expected in [('saffire-iv-vi:VI-3', 77), ('saffire-iv-vi:VI-4', 57)]:
    o = next(o for o in index[rid]['outcomes'] if o['quantity'] == 'max_temp_sfu_outlet')
    assert o['measure']['value'] == expected
    assert index[rid]['sources'][o['source']]['table'] == 'Table 2'

begin('', True, 'Challenge response: Flame in Freefall | NASA Space Apps 2026 | Independent project; no NASA endorsement')
text(72, 125, 'Flame\nFreefall', 118, WHITE, True, leading=1.0)
text(78, 405, 'Make NASA combustion evidence\nusable for the next research decision.', 39, WHITE, width=900)
text(78, 571, 'Find relevant experiments. Audit the comparison.\nExport the evidence and its limits.', 29, MUTED, width=920)
rect(1110, 150, 4, 560, '#49667D')
for yy, label, desc in [(185, 'Prevention', 'Material flammability'), (350, 'Detection', 'Smoke and sensors'), (515, 'Suppression', 'Droplet extinction')]:
    text(1160, yy, label, 32, WHITE, True, width=360)
    text(1160, yy+54, desc, 21, MUTED, width=360)
text(78, 733, 'Code Nashai  /  Muhammad Marjan Ahmed  /  Solo builder', 23, WHITE)
end('I am Muhammad Marjan Ahmed, the solo builder behind Code Nashai. Flame Freefall turns NASA combustion records into a traceable research workflow across prevention, detection and suppression. Our goal is to help researchers make a better-supported next research decision. This is an independent challenge response, not NASA-approved safety software.')

begin('The hard part is knowing what transfers.', source='Source: supplied challenge-details.md; NASA PSI investigations and governed source reports')
text(75, 230, 'A spacecraft-fire researcher asks:', 26, BLUE, True)
text(75, 287, 'Which experiments inform a study\nnear a proposed Lunar atmosphere?', 49, INK, True)
for x, head, body in [(75, 'Find', 'Tables and reports are\nspread across investigations.'), (575, 'Compare', 'Matching oxygen alone\ndoes not match the experiment.'), (1075, 'Interpret', 'A nearby result can still\nhave limited applicability.')]:
    rect(x, 493, 430, 5, BLUE)
    text(x, 533, head, 35, INK, True, width=430)
    text(x, 596, body, 26, INK, width=440)
text(75, 735, 'The opportunity: preserve context from the research question to the source.', 29, BLUE, True)
end('The challenge is not simply finding a paper. An engineer needs to know whether its experiment supports the question being asked. Fuel geometry, oxygen, pressure, flow and measurement methods matter. Microgravity findings do not automatically validate Lunar-gravity behavior. Flame Freefall makes those transfer limits visible.')

begin('One question. A traceable evidence dossier.', source='Implemented: system/site/app/decide; lib/decision.ts; lib/psi-comparison.ts; docs/evidence-method.md')
picture(OUT / 'assets/local-dossier-capture.png', 75, 240, 850, 537)
for yy, n, head, body in [(245, '1', 'Set the question', 'Choose job and conditions.'), (405, '2', 'Inspect the evidence', 'Check relevance and source limits.'), (565, '3', 'Keep the reasoning', 'Export settings, records and citations.')]:
    text(990, yy, n, 42, BLUE, True, width=60)
    text(1055, yy+3, head, 30, INK, True, width=465)
    text(990, yy+65, body, 24, INK, width=540)
text(75, 786, 'Actual local dossier capture, cropped from the saved workflow run; not a live deployment check.', 15, BLUE)
end('The working product records the research question verbatim. Explicit controls determine retrieval. Investigations have source-supported direct or indirect relevance assignments, and unmatched classifications remain visible as unknown. This is an actual cropped local browser capture from the saved implementation workflow; it is not a fresh live-site screenshot. The dossier retains the shortlist, settings, underlying records and dataset identity. The deterministic Explorer works without an AI service.')

begin('Demo: an atmosphere match is a starting point.', True, 'Local executable scenario: research/research-scenario-verification.json | Retrieval overlap is not safety or gravity validation')
text(75, 220, 'Research question', 24, MUTED, True)
text(75, 269, 'What informs a solid-material study\nnear a proposed Lunar atmosphere?', 43, WHITE, True)
rect(75, 410, 695, 230, '#1B3A53'); rect(800, 410, 725, 230, '#1B3A53')
text(105, 440, 'SAFFIRE IV–VI', 37, WHITE, True, width=630)
text(105, 503, 'Direct solid-fuel evidence.\nInspect setup and missing fields.', 28, WHITE, width=630)
text(830, 440, 'ACME BRE', 37, WHITE, True, width=650)
text(830, 503, 'Indirect condensed-fuel emulation.\nKeep its physical geometry distinct.', 28, WHITE, width=660)
text(80, 695, 'Widening the oxygen search window changes the retrieved evidence.', 30, WHITE, True)
text(80, 751, 'The experiment has not changed. Neither has its transfer limit.', 28, MUTED)
end('In the implemented Lunar scenario, shortlist SAFFIRE IV–VI and ACME BRE. SAFFIRE provides direct solid-fuel evidence; BRE is a gaseous experiment emulating aspects of condensed-fuel burning. Doubling the oxygen retrieval tolerance admits one full SAFFIRE record in the engineering scenario. That is sensitivity of evidence availability, not a safety margin. Then inspect an actual source-backed comparison.')

begin('Two temperatures. No invented conclusion.', source='NASA NTRS 20240002981, Table 2 | records saffire-iv-vi:VI-3 and VI-4 | Max temperature at SFU outlet')
for x, value, name in [(80, '77°C', 'VI-3 / two-sided PMMA'), (575, '57°C', 'VI-4 / one-sided PMMA')]:
    text(x, 242, value, 104, BLUE, True, width=470)
    text(x, 385, name, 28, INK, True, width=470)
text(80, 470, 'Reported observations from Table 2', 25, BLUE)
rect(1080, 235, 3, 395, LINE)
text(1120, 250, 'Audit the comparison', 28, INK, True, width=410)
text(1120, 313, 'Fuel description differs.\nOxygen and pressure differ.\nMethod and dimensions\nremain incomplete.', 25, INK, width=410, leading=1.5)
rect(75, 640, 1450, 125, NAVY)
text(110, 668, 'Inspect both results. Do not infer a controlled effect.', 37, WHITE, True)
end('The comparison audit surfaces two real outlet-temperature observations from SAFFIRE Table 2. It preserves their source identities and shows the setup differences. Because key metadata are missing and the conditions differ, it refuses a condition-matched claim. We do not subtract the temperatures or attribute the difference to specimen configuration. This is a useful source audit with an explicit next evidence check. Source: https://ntrs.nasa.gov/citations/20240002981')

begin('AI helps you ask. Code preserves the evidence.', source='Local dataset: psi-data/derived/runs.json | Safeguards: main.py, psi_query.py, turn_guard.py | Internal checks, not safety validation')
for x, num, label in [(75, '1,951', 'Indexed records'), (575, '1,838', 'Test / test-point records'), (1075, '23', 'Stable governed documents')]:
    text(x, 240, num, 78, BLUE, True, width=460)
    text(x, 347, label, 25, INK, width=460)
rect(75, 430, 1450, 2, LINE)
text(75, 480, 'Built to inspect', 32, INK, True)
text(75, 540, 'Source-linked normalization\nPython / TypeScript query parity\nDeterministic measurement widgets', 28, INK, width=710, leading=1.5)
text(875, 480, 'Boundaries stay visible', 32, INK, True, width=650)
text(875, 540, 'Missing metadata and source conflicts\nUnknown observation independence\nNo material-safety or prediction claim', 28, INK, width=650, leading=1.5)
end('NASA PSI tables and source reports feed source-preserving ingest, deterministic query twins, a static Next.js evidence interface, and optional FastAPI/ChatKit conversation. Structured PSI numbers render in code-owned widgets rather than generated prose. Narrative retrieval is separately cited. There are 1,951 indexed records; only 1,838 are individual test or test-point records, not proven independent replicates. Code was built with AI assistance; no independent expert or user validation is claimed.')

begin('Make the next research decision defensible.', True, 'Code Nashai | Muhammad Marjan Ahmed | Prior work disclosed in SUBMISSION.md; competition eligibility remains unresolved')
text(75, 235, 'For researchers and aerospace engineers', 34, WHITE, True)
text(75, 309, 'A source-backed shortlist.\nAn auditable comparison.\nA reproducible starting point.', 49, WHITE, True, leading=1.3)
rect(1000, 235, 3, 420, '#49667D')
text(1045, 250, 'Next: prove the benefit', 29, WHITE, True, width=480)
text(1045, 319, 'Observe researcher task completion.\nReview relevance with domain experts.\nResolve critical source metadata.', 24, MUTED, width=480, leading=1.6)
text(1045, 535, 'Try the evidence workflow', 27, WHITE, True, width=480)
text(1045, 590, '/decide/ → shortlist → audit → export', 23, WHITE, width=480)
text(75, 718, 'Project: github.com/marjan-ahmed/flame-freefall', 28, WHITE)
text(75, 767, 'Designed to support research; measured time savings and safety outcomes are not established.', 19, MUTED)
pdf.linkURL('https://github.com/marjan-ahmed/flame-freefall', (75, 125, 830, 190), relative=0)
end('Our intended contribution is a defensible starting point for spacecraft-fire research. The next milestone is observed task completion with researchers and independent domain review, not another feature count. Explore the repository for the implemented workflow and reproduction instructions. The project predates the event; organizer eligibility clarification remains unresolved. Team: Code Nashai. Solo builder: Muhammad Marjan Ahmed. No NASA endorsement, measured time-saving claim, or safety qualification is asserted.')

assert len(prs.slides) == 7
pdf.save()
prs.save(OUT / 'flame-freefall-pitch.pptx')
thumbs = []
for i in range(1, 8):
    p = Image.open(OUT / f'slide-{i:02}.png'); p.thumbnail((640, 360)); thumbs.append(p)
sheet = Image.new('RGB', (1280, 1440), '#D8E1E8')
for i, p in enumerate(thumbs): sheet.paste(p, ((i % 2)*640, (i//2)*360))
sheet.save(OUT / 'contact-sheet.png')
(OUT / 'speaker-notes.md').write_text('# Flame Freefall speaker notes\n\n' + '\n\n'.join(f'## Slide {i+1}\n\n{n}' for i, n in enumerate(notes)) + '\n', encoding='utf-8')
(OUT / 'build-receipt.json').write_text(json.dumps({'slides': 7, 'dataset_sha256': hashlib.sha256(bundle_bytes).hexdigest(), 'records': len(runs), 'test_and_test_point_records': individual, 'source_revision': '47cdf73', 'scope': 'Local code and data; no live application or deployment validation. Slides 4–5 are evidence walkthroughs, not UI screenshots.', 'artifacts': ['flame-freefall-pitch.pdf', 'flame-freefall-pitch.pptx'], 'claims_checked': ['record granularities', 'SAFFIRE Table 2 outlet temperatures and source indexes']}, indent=2)+'\n', encoding='utf-8')
print('Built seven slides: PDF, editable PowerPoint, PNG previews, speaker notes and claim receipt.')
