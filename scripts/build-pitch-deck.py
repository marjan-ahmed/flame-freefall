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
text(78, 405, 'Your AI research companion\nfor NASA combustion evidence.', 39, WHITE, width=900)
text(78, 571, 'Ask in natural language. Inspect cited evidence.\nCompare experiments. Export your research dossier.', 29, MUTED, width=920)
rect(1110, 150, 4, 560, '#49667D')
for yy, label, desc in [(185, 'Prevention', 'Material flammability'), (350, 'Detection', 'Smoke and sensors'), (515, 'Suppression', 'Droplet extinction')]:
    text(1160, yy, label, 32, WHITE, True, width=360)
    text(1160, yy+54, desc, 21, MUTED, width=360)
text(78, 733, 'Code Nashai  /  Muhammad Marjan Ahmed  /  Solo builder', 23, WHITE)
end('I am Muhammad Marjan Ahmed, the solo builder behind Code Nashai. Flame Freefall combines an AI-powered research chatbot with a traceable evidence workbench across prevention, detection and suppression. Ask questions in natural language, inspect source-linked test results and research documents, then use the workbench to compare and export evidence. This is an independent challenge response, not NASA-approved safety software.')

begin('The hard part is knowing what transfers.', source='Source: supplied challenge-details.md; NASA PSI investigations and governed source reports')
text(75, 230, 'A spacecraft-fire researcher asks:', 26, BLUE, True)
text(75, 287, 'Which experiments inform a study\nnear a proposed Lunar atmosphere?', 49, INK, True)
for x, head, body in [(75, 'Find', 'Tables and reports are\nspread across investigations.'), (575, 'Compare', 'Matching oxygen alone\ndoes not match the experiment.'), (1075, 'Interpret', 'A nearby result can still\nhave limited applicability.')]:
    rect(x, 493, 430, 5, BLUE)
    text(x, 533, head, 35, INK, True, width=430)
    text(x, 596, body, 26, INK, width=440)
text(75, 735, 'The opportunity: ask an AI companion, then inspect the evidence behind the answer.', 28, BLUE, True)
end('The challenge is not simply finding a paper. An engineer needs to know whether its experiment supports the question being asked. The AI chatbot provides a natural-language entry point into cited research and structured test tools. The evidence workbench then exposes conditions, missing fields and transfer limits. Microgravity findings do not automatically validate Lunar-gravity behavior.')

begin('Ask in chat. Investigate in the workbench.', source='Implemented: ChatKit UI and PSI tools; /decide dossier; query and comparison twins; docs/evidence-method.md')
picture(OUT / 'assets/local-dossier-capture.png', 75, 240, 850, 537)
for yy, n, head, body in [(245, '1', 'Ask the AI chatbot', 'Search research and test records.'), (405, '2', 'Inspect the evidence', 'Check conditions and source limits.'), (565, '3', 'Build your dossier', 'Use the workbench to shortlist and export.')]:
    text(990, yy, n, 42, BLUE, True, width=60)
    text(1055, yy+3, head, 30, INK, True, width=465)
    text(990, yy+65, body, 24, INK, width=540)
text(75, 786, 'Actual local dossier capture, cropped from the saved workflow run; not a live deployment check.', 15, BLUE)
end('The chatbot and evidence workbench are complementary interfaces to the project. Ask the chatbot to find tests, explain cited research, show plots or audit records. In the workbench, explicitly set conditions, shortlist investigations and export a reproducible dossier. This does not claim that a chat conversation automatically becomes a dossier. The screenshot is an actual saved local capture of the dossier UI. The deterministic Explorer works without an AI service.')

begin('From a question to evidence you can inspect.', True, 'Example chat prompt + local workbench scenario | Retrieval overlap is not safety or gravity validation')
text(75, 220, 'Ask the AI chatbot', 24, MUTED, True)
text(75, 269, 'Show solid material tests\nnear a Lunar atmosphere.', 43, WHITE, True)
rect(75, 410, 695, 230, '#1B3A53'); rect(800, 410, 725, 230, '#1B3A53')
text(105, 440, 'SAFFIRE IV–VI', 37, WHITE, True, width=630)
text(105, 503, 'Direct solid-fuel evidence.\nInspect setup and missing fields.', 28, WHITE, width=630)
text(830, 440, 'ACME BRE', 37, WHITE, True, width=650)
text(830, 503, 'Indirect condensed-fuel emulation.\nKeep its physical geometry distinct.', 28, WHITE, width=660)
text(80, 695, 'Widening the oxygen search window changes the retrieved evidence.', 30, WHITE, True)
text(80, 751, 'The experiment has not changed. Neither has its transfer limit.', 28, MUTED)
end('The displayed prompt is an example of an explicit natural-language condition search, not a transcript of a newly recorded provider session. The chatbot can render test-search widgets with conditions and source records. Continue the research in the workbench, where SAFFIRE IV–VI provides direct solid-fuel evidence and BRE offers indirect condensed-fuel emulation. Doubling the oxygen search tolerance admits one full SAFFIRE record in the saved engineering scenario. These are separate chat and workbench capabilities, not an automatic end-to-end handoff.')

begin('Compare with evidence. Keep the context.', source='NASA NTRS 20240002981, Table 2 | records saffire-iv-vi:VI-3 and VI-4 | Max temperature at SFU outlet')
for x, value, name in [(80, '77°C', 'VI-3 / two-sided PMMA'), (575, '57°C', 'VI-4 / one-sided PMMA')]:
    text(x, 242, value, 104, BLUE, True, width=470)
    text(x, 385, name, 28, INK, True, width=470)
text(80, 470, 'Reported observations from Table 2', 25, BLUE)
rect(1080, 235, 3, 395, LINE)
text(1120, 250, 'Chat + Explorer audits', 28, INK, True, width=410)
text(1120, 313, 'Fuel description differs.\nOxygen and pressure differ.\nMethod and dimensions\nremain incomplete.', 25, INK, width=410, leading=1.5)
rect(75, 640, 1450, 125, NAVY)
text(110, 668, 'Inspect both results. Do not infer a controlled effect.', 37, WHITE, True)
end('The chatbot has a two-record comparison tool; the Explorer provides a detailed audit interface. The source-backed example shows outlet temperatures from SAFFIRE Table 2 and the reasons a condition-matched comparison is blocked. Missing metadata and differing conditions remain visible. We do not subtract the temperatures or attribute their difference to specimen configuration. Source: https://ntrs.nasa.gov/citations/20240002981')

begin('Meet your AI combustion research companion.', source='Implemented: psi_tools.py, psi_widgets.py, main.py and ChatKit UI | Tool capabilities; no universal answer-correctness claim')
text(75, 230, 'Find and understand', 34, BLUE, True, width=680)
text(75, 300, 'Ask questions in natural language.\nRetrieve cited research documents.\nFind tests by fuel and conditions.\nOpen individual records and sources.', 29, INK, width=680, leading=1.6)
text(855, 230, 'Explore and compare', 34, BLUE, True, width=680)
text(855, 300, 'Plot measured outcomes.\nInspect gap maps and atmosphere coverage.\nCompare investigations and test records.\nOrder eligible individual measurements.', 29, INK, width=680, leading=1.6)
rect(75, 548, 1450, 139, NAVY)
text(110, 570, 'Natural-language question → research tools → source-linked widgets', 32, WHITE, True)
text(110, 630, 'Code renders PSI measurements; narrative research answers carry source citations.', 26, WHITE)
text(75, 731, '1,951 indexed records  /  1,838 test or test-point records  /  23 stable documents', 27, BLUE, True)
text(75, 779, 'Missing metadata stays visible. Coverage and measurement ordering do not establish safety.', 20, INK)
end('The AI-powered chatbot is built with ChatKit, FastAPI and an agent with eight local PSI tools plus cited narrative retrieval through MCP. Features include natural-language test searches, gap maps, investigation comparisons, individual test details, plots, ordering eligible measurements, atmosphere coverage and two-record comparison audits. PSI numerical answers are rendered by deterministic widgets rather than model-generated numerical prose. Ambiguous condition requests can require explicit Explorer controls. The dataset contains 1,951 indexed records, of which 1,838 are test or test-point records; these are not proven independent replicates. No universal answer accuracy, safety prediction or best-material claim is asserted.')

begin('Ask better questions. Keep the evidence.', True, 'Code Nashai | Muhammad Marjan Ahmed | Solo builder | Flame in Freefall challenge response')
text(75, 235, 'For researchers and aerospace engineers', 34, WHITE, True)
text(75, 309, 'An AI research conversation.\nA source-backed comparison.\nA reproducible evidence dossier.', 46, WHITE, True, leading=1.3)
rect(1000, 235, 3, 420, '#49667D')
text(1045, 250, 'Next: prove the benefit', 29, WHITE, True, width=480)
text(1045, 319, 'Observe researcher task completion.\nReview relevance with domain experts.\nResolve critical source metadata.', 24, MUTED, width=480, leading=1.6)
text(1045, 535, 'Explore Flame Freefall', 27, WHITE, True, width=480)
text(1045, 590, 'AI chatbot + Explorer + evidence dossier', 23, WHITE, width=480)
text(75, 718, 'From NASA combustion data to questions worth investigating.', 28, WHITE)
text(75, 767, 'Designed to support research; measured time savings and safety outcomes are not established.', 19, MUTED)
end('Flame Freefall combines an AI research companion, an Explorer and reproducible evidence dossiers. It is designed to help researchers find and inspect applicable evidence before the next study. The next milestone is observed task completion with researchers and independent domain review. Team: Code Nashai. Solo builder: Muhammad Marjan Ahmed. No measured time-saving or safety-qualification claim is asserted.')

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
