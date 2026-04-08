"""
Generate a professional criminology lecture PPT:
Rational Choice & Routine Activity Theory
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
import math

# ── Constants ──────────────────────────────────────────────────────────
NAVY   = RGBColor(0x1B, 0x2A, 0x44)
GOLD   = RGBColor(0xC8, 0xA8, 0x4B)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
DARK   = RGBColor(0x2A, 0x2A, 0x2A)
LIGHT_BG = RGBColor(0xF5, 0xF3, 0xEE)
LIGHT_NAVY = RGBColor(0x2D, 0x3E, 0x5A)
GOLD_DARK = RGBColor(0xA0, 0x86, 0x3C)

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

FONT_TITLE = "Calibri"
FONT_BODY  = "Calibri"

prs = Presentation()
prs.slide_width  = SLIDE_W
prs.slide_height = SLIDE_H

# Use blank layout
blank_layout = prs.slide_layouts[6]

slide_number_counter = [0]

# ── Helper functions ───────────────────────────────────────────────────

def add_slide():
    slide_number_counter[0] += 1
    return prs.slides.add_slide(blank_layout)

def fill_bg(slide, color):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_textbox(slide, left, top, width, height, text, font_size=18,
                bold=False, color=DARK, alignment=PP_ALIGN.LEFT,
                font_name=FONT_BODY, line_spacing=1.2):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.bold = bold
    p.font.color.rgb = color
    p.font.name = font_name
    p.alignment = alignment
    p.space_after = Pt(4)
    if line_spacing != 1.0:
        p.line_spacing = Pt(font_size * line_spacing)
    return tf

def add_para(tf, text, font_size=18, bold=False, color=DARK,
             alignment=PP_ALIGN.LEFT, font_name=FONT_BODY,
             space_before=0, space_after=6, bullet=False, level=0):
    p = tf.add_paragraph()
    p.text = text
    p.font.size = Pt(font_size)
    p.font.bold = bold
    p.font.color.rgb = color
    p.font.name = font_name
    p.alignment = alignment
    p.space_before = Pt(space_before)
    p.space_after = Pt(space_after)
    p.level = level
    if bullet:
        p.level = level
    return p

def add_gold_line(slide, left, top, width, height=Pt(2)):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = GOLD
    shape.line.fill.background()
    return shape

def add_slide_number(slide, num, color=GOLD):
    txBox = slide.shapes.add_textbox(
        SLIDE_W - Inches(1.0), SLIDE_H - Inches(0.5),
        Inches(0.8), Inches(0.35)
    )
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    p.text = str(num)
    p.font.size = Pt(11)
    p.font.color.rgb = color
    p.font.name = FONT_BODY
    p.alignment = PP_ALIGN.RIGHT

def add_gold_bottom_line(slide):
    add_gold_line(slide, Inches(0.5), SLIDE_H - Inches(0.6), SLIDE_W - Inches(1.0), Pt(1.5))

def add_shape_rect(slide, left, top, width, height, fill_color, line_color=None):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    if line_color:
        shape.line.color.rgb = line_color
        shape.line.width = Pt(1.5)
    else:
        shape.line.fill.background()
    return shape

def add_rounded_rect(slide, left, top, width, height, fill_color, line_color=None):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    if line_color:
        shape.line.color.rgb = line_color
        shape.line.width = Pt(1.5)
    else:
        shape.line.fill.background()
    return shape

def set_shape_text(shape, text, font_size=14, bold=False, color=WHITE,
                   alignment=PP_ALIGN.CENTER, font_name=FONT_BODY, anchor=MSO_ANCHOR.MIDDLE):
    tf = shape.text_frame
    tf.word_wrap = True
    tf.paragraphs[0].alignment = alignment
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.bold = bold
    p.font.color.rgb = color
    p.font.name = font_name
    tf.vertical_anchor = anchor

def content_slide_header(slide, title_text):
    """Standard content slide: light bg, navy header bar, gold line, slide number."""
    fill_bg(slide, LIGHT_BG)
    # Header bar
    header = add_shape_rect(slide, Inches(0), Inches(0), SLIDE_W, Inches(1.2), NAVY)
    set_shape_text(header, title_text, font_size=28, bold=True, color=WHITE,
                   alignment=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.MIDDLE)
    header.text_frame.paragraphs[0].font.name = FONT_TITLE
    # indent text
    header.text_frame.margin_left = Inches(0.8)
    # Gold accent line under header
    add_gold_line(slide, Inches(0), Inches(1.2), SLIDE_W, Pt(3))
    # Bottom gold line & slide number
    add_gold_bottom_line(slide)
    add_slide_number(slide, slide_number_counter[0], GOLD_DARK)

def add_bullet_list(slide, items, left=Inches(0.9), top=Inches(1.7),
                    width=Inches(11.0), font_size=18, color=DARK, spacing=8, bold_first=False):
    """Add a bulleted list. If bold_first, bold text before first colon."""
    height = Inches(5.0)
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(spacing)
        p.font.size = Pt(font_size)
        p.font.color.rgb = color
        p.font.name = FONT_BODY
        p.alignment = PP_ALIGN.LEFT
        p.level = 0

        if bold_first and ":" in item:
            # Split at first colon
            parts = item.split(":", 1)
            run1 = p.add_run()
            run1.text = "\u2022  " + parts[0] + ":"
            run1.font.size = Pt(font_size)
            run1.font.bold = True
            run1.font.color.rgb = color
            run1.font.name = FONT_BODY
            run2 = p.add_run()
            run2.text = parts[1]
            run2.font.size = Pt(font_size)
            run2.font.bold = False
            run2.font.color.rgb = color
            run2.font.name = FONT_BODY
        else:
            p.text = "\u2022  " + item
    return tf

# ══════════════════════════════════════════════════════════════════════
# SLIDE 1: Title Slide
# ══════════════════════════════════════════════════════════════════════
s = add_slide()
fill_bg(s, NAVY)

# Gold decorative line at top
add_gold_line(s, Inches(1.5), Inches(1.8), Inches(10.3), Pt(2))

# Title
add_textbox(s, Inches(1.5), Inches(2.0), Inches(10.3), Inches(1.6),
            "Rational Choice &\nRoutine Activity Theory",
            font_size=42, bold=True, color=WHITE, alignment=PP_ALIGN.CENTER,
            font_name=FONT_TITLE, line_spacing=1.15)

# Gold line under title
add_gold_line(s, Inches(4.5), Inches(3.75), Inches(4.3), Pt(2))

# Subtitle
add_textbox(s, Inches(1.5), Inches(4.0), Inches(10.3), Inches(0.6),
            "Cornish & Clarke  \u00b7  Cohen & Felson  (1970s\u201380s)",
            font_size=20, bold=False, color=GOLD, alignment=PP_ALIGN.CENTER)

# Lecture info
add_textbox(s, Inches(1.5), Inches(4.7), Inches(10.3), Inches(0.5),
            "Lecture 8  \u00b7  Environmental Criminology",
            font_size=16, bold=False, color=RGBColor(0xAA, 0xAA, 0xBB),
            alignment=PP_ALIGN.CENTER)

# Bottom gold line
add_gold_line(s, Inches(1.5), Inches(5.5), Inches(10.3), Pt(2))

add_slide_number(s, slide_number_counter[0], GOLD)

# ══════════════════════════════════════════════════════════════════════
# SLIDE 2: Overview
# ══════════════════════════════════════════════════════════════════════
s = add_slide()
content_slide_header(s, "Overview")

# Roadmap boxes
labels = ["Rational Choice\nTheory", "Routine Activity\nTheory", "Key Research\n& Evidence", "Policy &\nApplications"]
for i, label in enumerate(labels):
    x = Inches(1.0 + i * 2.9)
    y = Inches(2.5)
    box = add_rounded_rect(s, x, y, Inches(2.4), Inches(1.6), NAVY, GOLD)
    set_shape_text(box, label, font_size=18, bold=True, color=WHITE)
    # Number circle
    circle = slide_shapes = s.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(0.85), Inches(1.8), Inches(0.7), Inches(0.7))
    circle.fill.solid()
    circle.fill.fore_color.rgb = GOLD
    circle.line.fill.background()
    set_shape_text(circle, str(i+1), font_size=20, bold=True, color=NAVY)

# Arrow connectors (simple rectangles)
for i in range(3):
    x = Inches(3.4 + i * 2.9)
    arr = add_shape_rect(s, x, Inches(3.15), Inches(0.5), Pt(3), GOLD)

# Bottom note
add_textbox(s, Inches(1.0), Inches(4.8), Inches(11.0), Inches(0.5),
            "Each section builds on the previous \u2014 from theory to evidence to practice.",
            font_size=15, color=RGBColor(0x66, 0x66, 0x66), alignment=PP_ALIGN.CENTER)

# ══════════════════════════════════════════════════════════════════════
# SLIDE 3: Classical Roots
# ══════════════════════════════════════════════════════════════════════
s = add_slide()
content_slide_header(s, "Classical Roots")

items = [
    "Both theories trace back to the Classical School of criminology (18th century)",
    "Cesare Beccaria (1764): Punishment should be swift, certain, and proportional",
    "Jeremy Bentham: \"Felicific calculus\" \u2014 people seek pleasure and avoid pain",
    "Core assumption: Offenders are rational actors who make choices",
    "Crime is a product of free will, not fate or pathology",
    "Modern rational choice theory updates these ideas with cognitive psychology"
]
add_bullet_list(s, items, font_size=19, spacing=12)

# ══════════════════════════════════════════════════════════════════════
# SLIDE 4: Rational Choice Theory: Core
# ══════════════════════════════════════════════════════════════════════
s = add_slide()
content_slide_header(s, "Rational Choice Theory: Core Principles")

# Left side - main points
items = [
    "Offenders weigh perceived costs against perceived benefits before acting",
    "Bounded rationality (Herbert Simon, 1957): decisions made with limited information, time, and cognitive capacity",
    "Not perfectly rational, but reasoning within situational constraints",
    "Decisions are crime-specific \u2014 burglary vs. robbery involve different calculus",
    "Situational factors heavily influence the decision to offend"
]
add_bullet_list(s, items, font_size=18, spacing=10, width=Inches(7.5))

# Right side - visual box
box = add_rounded_rect(s, Inches(9.0), Inches(2.0), Inches(3.5), Inches(4.0), NAVY, GOLD)
tf = box.text_frame
tf.word_wrap = True
tf.vertical_anchor = MSO_ANCHOR.MIDDLE
p = tf.paragraphs[0]
p.text = "Decision Calculus"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = GOLD
p.font.name = FONT_TITLE
p.alignment = PP_ALIGN.CENTER

for txt in ["\nPerceived Benefits", "  \u2022 Money / Thrill / Status",
            "\n     vs.", "\nPerceived Costs", "  \u2022 Arrest / Punishment / Shame"]:
    pp = tf.add_paragraph()
    pp.text = txt
    pp.font.size = Pt(13)
    pp.font.bold = "vs." in txt or txt.startswith("\nPerceived")
    pp.font.color.rgb = WHITE if "vs." not in txt else GOLD
    pp.font.name = FONT_BODY
    pp.alignment = PP_ALIGN.CENTER

# ══════════════════════════════════════════════════════════════════════
# SLIDE 5: Decision Types
# ══════════════════════════════════════════════════════════════════════
s = add_slide()
content_slide_header(s, "Decision Types (Cornish & Clarke, 1986)")

# Two columns
# Left box - Involvement
box1 = add_rounded_rect(s, Inches(0.9), Inches(1.8), Inches(5.4), Inches(4.5), WHITE, NAVY)
tf1 = box1.text_frame
tf1.word_wrap = True
tf1.margin_left = Inches(0.3)
tf1.margin_top = Inches(0.2)
p = tf1.paragraphs[0]
p.text = "Involvement Decisions"
p.font.size = Pt(22)
p.font.bold = True
p.font.color.rgb = NAVY
p.font.name = FONT_TITLE
p.alignment = PP_ALIGN.CENTER

for txt in ["Whether to begin offending (initiation)",
            "Whether to continue offending (habituation)",
            "Whether to stop offending (desistance)",
            "",
            "Influenced by background factors,\nlearning, and life circumstances"]:
    pp = tf1.add_paragraph()
    pp.text = ("\u2022  " + txt) if txt and not txt.startswith("Influenced") else txt
    pp.font.size = Pt(15)
    pp.font.color.rgb = DARK
    pp.font.name = FONT_BODY
    pp.alignment = PP_ALIGN.LEFT
    pp.space_after = Pt(6)
    if txt.startswith("Influenced"):
        pp.font.italic = True
        pp.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

# Right box - Event
box2 = add_rounded_rect(s, Inches(7.0), Inches(1.8), Inches(5.4), Inches(4.5), WHITE, GOLD_DARK)
tf2 = box2.text_frame
tf2.word_wrap = True
tf2.margin_left = Inches(0.3)
tf2.margin_top = Inches(0.2)
p = tf2.paragraphs[0]
p.text = "Event Decisions"
p.font.size = Pt(22)
p.font.bold = True
p.font.color.rgb = GOLD_DARK
p.font.name = FONT_TITLE
p.alignment = PP_ALIGN.CENTER

for txt in ["When to commit this specific crime",
            "Where to commit it (target selection)",
            "How to carry it out (modus operandi)",
            "",
            "Influenced by immediate situational\nfactors and opportunities"]:
    pp = tf2.add_paragraph()
    pp.text = ("\u2022  " + txt) if txt and not txt.startswith("Influenced") else txt
    pp.font.size = Pt(15)
    pp.font.color.rgb = DARK
    pp.font.name = FONT_BODY
    pp.alignment = PP_ALIGN.LEFT
    pp.space_after = Pt(6)
    if txt.startswith("Influenced"):
        pp.font.italic = True
        pp.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

# ══════════════════════════════════════════════════════════════════════
# SLIDE 6: Situational Crime Prevention (25 Techniques)
# ══════════════════════════════════════════════════════════════════════
s = add_slide()
content_slide_header(s, "Situational Crime Prevention: 25 Techniques")

categories = [
    ("Increase\nEffort", NAVY, ["Target hardening", "Access control", "Screen exits", "Deflect offenders", "Control tools"]),
    ("Increase\nRisk", LIGHT_NAVY, ["Extend guardianship", "Assist surveillance", "Reduce anonymity", "Place managers", "Formal surveillance"]),
    ("Reduce\nRewards", RGBColor(0x3D, 0x5A, 0x3D), ["Conceal targets", "Remove targets", "Identify property", "Disrupt markets", "Deny benefits"]),
    ("Reduce\nProvocations", RGBColor(0x6B, 0x3A, 0x2A), ["Reduce frustration", "Avoid disputes", "Reduce temptation", "Neutralize pressure", "Discourage imitation"]),
    ("Remove\nExcuses", RGBColor(0x4A, 0x3A, 0x5A), ["Set rules", "Post instructions", "Alert conscience", "Assist compliance", "Control substances"]),
]

col_w = Inches(2.3)
start_x = Inches(0.6)
for i, (cat_name, cat_color, techniques) in enumerate(categories):
    x = start_x + i * (col_w + Inches(0.15))
    # Header
    hdr = add_shape_rect(s, x, Inches(1.6), col_w, Inches(0.9), cat_color)
    set_shape_text(hdr, cat_name, font_size=13, bold=True, color=WHITE)
    # Technique rows
    for j, tech in enumerate(techniques):
        y = Inches(2.55) + j * Inches(0.7)
        row_color = WHITE if j % 2 == 0 else RGBColor(0xE8, 0xE5, 0xDD)
        row = add_shape_rect(s, x, y, col_w, Inches(0.65), row_color)
        row.line.color.rgb = RGBColor(0xDD, 0xDD, 0xDD)
        row.line.width = Pt(0.5)
        set_shape_text(row, tech, font_size=11, bold=False, color=DARK)

# Source
add_textbox(s, Inches(0.9), Inches(6.3), Inches(11.0), Inches(0.4),
            "Clarke (1997); Cornish & Clarke (2003)",
            font_size=12, color=RGBColor(0x88, 0x88, 0x88), alignment=PP_ALIGN.LEFT)

# ══════════════════════════════════════════════════════════════════════
# SLIDE 7: Routine Activity Theory: Core
# ══════════════════════════════════════════════════════════════════════
s = add_slide()
content_slide_header(s, "Routine Activity Theory: Core")

items = [
    "Cohen & Felson (1979): \"Social Change and Crime Rate Trends\"",
    "Crime is a normal function of everyday life patterns, not pathological behavior",
    "Crime occurs when three elements converge in time and space:",
]
add_bullet_list(s, items, font_size=19, spacing=10, top=Inches(1.7))

# Three element boxes
labels_rat = [
    ("Motivated\nOffender", NAVY),
    ("Suitable\nTarget", RGBColor(0x6B, 0x3A, 0x2A)),
    ("Absence of Capable\nGuardian", RGBColor(0x3D, 0x5A, 0x3D))
]
for i, (lbl, clr) in enumerate(labels_rat):
    x = Inches(1.5 + i * 3.8)
    box = add_rounded_rect(s, x, Inches(3.8), Inches(3.0), Inches(1.3), clr, GOLD)
    set_shape_text(box, lbl, font_size=18, bold=True, color=WHITE)

# Plus signs and equals
add_textbox(s, Inches(4.5), Inches(4.0), Inches(0.5), Inches(0.8),
            "+", font_size=30, bold=True, color=GOLD, alignment=PP_ALIGN.CENTER)
add_textbox(s, Inches(8.3), Inches(4.0), Inches(0.5), Inches(0.8),
            "+", font_size=30, bold=True, color=GOLD, alignment=PP_ALIGN.CENTER)

# Bottom note
add_textbox(s, Inches(0.9), Inches(5.5), Inches(11.0), Inches(0.5),
            "Key insight: You don't need to explain criminal motivation to explain crime patterns.",
            font_size=16, bold=True, color=NAVY, alignment=PP_ALIGN.CENTER)

# ══════════════════════════════════════════════════════════════════════
# SLIDE 8: Crime Triangle
# ══════════════════════════════════════════════════════════════════════
s = add_slide()
content_slide_header(s, "The Crime Triangle (Problem Analysis Triangle)")

# Draw triangles using shapes - inner triangle
# Center of slide area
cx, cy = Inches(5.5), Inches(4.2)

# Inner triangle - three boxes positioned as triangle vertices
# Top vertex
top_box = add_rounded_rect(s, Inches(4.4), Inches(1.7), Inches(2.2), Inches(0.9), NAVY, GOLD)
set_shape_text(top_box, "Motivated\nOffender", font_size=14, bold=True, color=WHITE)

# Bottom-left
bl_box = add_rounded_rect(s, Inches(2.0), Inches(4.5), Inches(2.2), Inches(0.9), NAVY, GOLD)
set_shape_text(bl_box, "Suitable\nTarget", font_size=14, bold=True, color=WHITE)

# Bottom-right
br_box = add_rounded_rect(s, Inches(6.8), Inches(4.5), Inches(2.2), Inches(0.9), NAVY, GOLD)
set_shape_text(br_box, "Absence of\nGuardian", font_size=14, bold=True, color=WHITE)

# Center label
center_box = add_shape_rect(s, Inches(4.5), Inches(3.5), Inches(2.0), Inches(0.7), GOLD)
set_shape_text(center_box, "CRIME", font_size=18, bold=True, color=NAVY)

# Outer triangle (Eck's) - labels
# Handler (controls offender) - top-right of offender
add_textbox(s, Inches(6.8), Inches(1.7), Inches(2.5), Inches(0.9),
            "Handler\n(supervises offender)",
            font_size=14, bold=True, color=RGBColor(0x8B, 0x4D, 0x1A), alignment=PP_ALIGN.LEFT)

# Manager (controls place) - bottom center
add_textbox(s, Inches(4.2), Inches(5.6), Inches(2.6), Inches(0.9),
            "Place Manager\n(controls location)",
            font_size=14, bold=True, color=RGBColor(0x3D, 0x5A, 0x3D), alignment=PP_ALIGN.CENTER)

# Guardian (protects target) - bottom-left
add_textbox(s, Inches(0.3), Inches(4.5), Inches(2.0), Inches(0.9),
            "Guardian\n(protects target)",
            font_size=14, bold=True, color=RGBColor(0x4A, 0x3A, 0x6A), alignment=PP_ALIGN.LEFT)

# Right side explanation
right_tf = add_textbox(s, Inches(9.5), Inches(1.8), Inches(3.5), Inches(4.5),
                        "Eck's Extended Triangle", font_size=18, bold=True, color=NAVY)
for txt in [
    "\nInner triangle: three elements needed for crime",
    "\nOuter triangle: three controllers who can prevent it",
    "\nHandler: someone who knows the offender (parent, teacher, employer)",
    "\nManager: person responsible for the place (owner, janitor)",
    "\nGuardian: person who can protect the target (friend, police, bystander)"
]:
    pp = right_tf.add_paragraph()
    pp.text = txt
    pp.font.size = Pt(12)
    pp.font.color.rgb = DARK
    pp.font.name = FONT_BODY
    pp.space_after = Pt(2)

# ══════════════════════════════════════════════════════════════════════
# SLIDE 9: VIVA Model
# ══════════════════════════════════════════════════════════════════════
s = add_slide()
content_slide_header(s, "VIVA: What Makes a Target \"Suitable\"?")

viva = [
    ("V", "Value", "Target has value to the offender\n(monetary, symbolic, emotional)"),
    ("I", "Inertia", "Target is light, movable, easy to carry\n(a laptop vs. a grand piano)"),
    ("V", "Visibility", "Target is visible and known to offenders\n(items left in plain sight)"),
    ("A", "Access", "Target is accessible and unprotected\n(unlocked car, open window)"),
]

for i, (letter, word, desc) in enumerate(viva):
    y = Inches(1.8) + i * Inches(1.3)
    # Letter circle
    circle = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(1.0), y, Inches(0.9), Inches(0.9))
    circle.fill.solid()
    circle.fill.fore_color.rgb = NAVY
    circle.line.color.rgb = GOLD
    circle.line.width = Pt(2)
    set_shape_text(circle, letter, font_size=28, bold=True, color=GOLD)
    # Word
    add_textbox(s, Inches(2.2), y + Inches(0.05), Inches(2.5), Inches(0.5),
                word, font_size=22, bold=True, color=NAVY)
    # Description
    add_textbox(s, Inches(4.8), y + Inches(0.0), Inches(7.5), Inches(0.9),
                desc, font_size=15, color=DARK)

# Source
add_textbox(s, Inches(0.9), Inches(6.3), Inches(11.0), Inches(0.4),
            "Cohen & Felson (1979); also known as CRAVED (Clarke, 1999): Concealable, Removable, Available, Valuable, Enjoyable, Disposable",
            font_size=11, color=RGBColor(0x88, 0x88, 0x88))

# ══════════════════════════════════════════════════════════════════════
# SLIDE 10: Social Change & Crime
# ══════════════════════════════════════════════════════════════════════
s = add_slide()
content_slide_header(s, "Social Change & Crime Rates")

items = [
    "Felson & Cohen (1980): post-WWII social transformations increased crime",
    "More women entering the workforce \u2192 homes left empty during the day \u2192 reduced guardianship",
    "Growth of consumer electronics \u2192 more lightweight, valuable, portable targets",
    "Suburban sprawl \u2192 increased routine travel \u2192 more exposure to motivated offenders",
    "Rising affluence \u2192 more goods worth stealing",
    "Paradox: Social progress created more criminal opportunities",
]
add_bullet_list(s, items, font_size=18, spacing=12)

# Highlight box
box = add_rounded_rect(s, Inches(2.0), Inches(5.5), Inches(9.3), Inches(0.9), NAVY)
set_shape_text(box,
    "Key insight: Crime rose not because people became more criminal, but because opportunities multiplied.",
    font_size=15, bold=True, color=GOLD)

# ══════════════════════════════════════════════════════════════════════
# SLIDE 11: Hot Spots Research
# ══════════════════════════════════════════════════════════════════════
s = add_slide()
content_slide_header(s, "Key Research: Hot Spots of Crime")

items = [
    "Sherman, Gartin & Buerger (1989): Minneapolis hot spots study",
    "3.5% of addresses produced 50% of all calls for police service",
    "Crime is not randomly distributed \u2014 it clusters in specific micro-locations",
    "Braga et al. (2014): Meta-analysis of 25 experimental studies",
    "Hot spots policing produces statistically significant reductions in crime",
    "Effect sizes are modest but consistent across diverse settings",
    "Weisburd (2015): The \"law of crime concentration\" \u2014 crime concentrates at places"
]
add_bullet_list(s, items, font_size=17, spacing=10, bold_first=False)

# Stat highlight boxes
stats = [("3.5%", "of addresses"), ("50%", "of crime calls"), ("25", "studies reviewed")]
for i, (num, label) in enumerate(stats):
    x = Inches(2.0 + i * 3.5)
    box = add_rounded_rect(s, x, Inches(5.4), Inches(2.5), Inches(1.0), NAVY, GOLD)
    tf_s = box.text_frame
    tf_s.word_wrap = True
    tf_s.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf_s.paragraphs[0]
    p.text = num
    p.font.size = Pt(24)
    p.font.bold = True
    p.font.color.rgb = GOLD
    p.font.name = FONT_TITLE
    p.alignment = PP_ALIGN.CENTER
    pp = tf_s.add_paragraph()
    pp.text = label
    pp.font.size = Pt(12)
    pp.font.color.rgb = WHITE
    pp.font.name = FONT_BODY
    pp.alignment = PP_ALIGN.CENTER

# ══════════════════════════════════════════════════════════════════════
# SLIDE 12: Displacement
# ══════════════════════════════════════════════════════════════════════
s = add_slide()
content_slide_header(s, "Key Research: Does Crime Just Move?")

items = [
    "Displacement: the concern that preventing crime in one area simply moves it elsewhere",
    "Six types: temporal, spatial, target, tactical, offense, perpetrator",
    "",
    "Guerette & Bowers (2009): Systematic review of 102 evaluations:",
]
add_bullet_list(s, items, font_size=17, spacing=8)

# Key findings boxes
findings = [
    ("26%", "showed some\ndisplacement", RGBColor(0x8B, 0x3A, 0x3A)),
    ("27%", "showed diffusion\nof benefits", RGBColor(0x3D, 0x5A, 0x3D)),
    ("~50%", "showed no\ndisplacement at all", NAVY),
]
for i, (num, label, clr) in enumerate(findings):
    x = Inches(1.5 + i * 3.8)
    box = add_rounded_rect(s, x, Inches(3.8), Inches(3.0), Inches(1.6), clr, GOLD)
    tf_s = box.text_frame
    tf_s.word_wrap = True
    tf_s.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf_s.paragraphs[0]
    p.text = num
    p.font.size = Pt(30)
    p.font.bold = True
    p.font.color.rgb = GOLD
    p.font.name = FONT_TITLE
    p.alignment = PP_ALIGN.CENTER
    pp = tf_s.add_paragraph()
    pp.text = label
    pp.font.size = Pt(14)
    pp.font.color.rgb = WHITE
    pp.font.name = FONT_BODY
    pp.alignment = PP_ALIGN.CENTER

# Bottom note
add_textbox(s, Inches(0.9), Inches(5.8), Inches(11.0), Inches(0.5),
            "Weisburd et al. (2006): Crime prevention benefits outweigh any displacement that occurs.",
            font_size=15, bold=True, color=NAVY, alignment=PP_ALIGN.CENTER)

# ══════════════════════════════════════════════════════════════════════
# SLIDE 13: Theory Comparisons
# ══════════════════════════════════════════════════════════════════════
s = add_slide()
content_slide_header(s, "Theory Comparisons")

# Table header
headers = ["", "Rational Choice", "Social Bond Theory", "General Strain Theory"]
col_widths = [Inches(2.2), Inches(3.3), Inches(3.3), Inches(3.3)]
col_x = [Inches(0.6)]
for w in col_widths[:-1]:
    col_x.append(col_x[-1] + w + Inches(0.08))

for i, hdr in enumerate(headers):
    box = add_shape_rect(s, col_x[i], Inches(1.6), col_widths[i], Inches(0.7),
                         NAVY if i > 0 else GOLD)
    set_shape_text(box, hdr, font_size=14, bold=True, color=WHITE if i > 0 else NAVY)

rows = [
    ("Focus", "Opportunity &\nSituation", "Social bonds &\nConformity", "Strain, stress &\nNegative emotions"),
    ("Key Question", "When and where\ndoes crime occur?", "Why do people\nconform?", "Why do people\noffend?"),
    ("Unit of\nAnalysis", "Crime event", "Individual", "Individual"),
    ("Key Scholars", "Cornish & Clarke;\nCohen & Felson", "Hirschi (1969)", "Agnew (1992);\nMerton (1938)"),
    ("Policy Focus", "Situational\nprevention", "Strengthen bonds\n(family, school)", "Reduce strain;\nequal opportunity"),
]

for j, (label, *cells) in enumerate(rows):
    y = Inches(2.38) + j * Inches(0.95)
    bg = WHITE if j % 2 == 0 else RGBColor(0xE8, 0xE5, 0xDD)
    # Label col
    box = add_shape_rect(s, col_x[0], y, col_widths[0], Inches(0.9), GOLD)
    set_shape_text(box, label, font_size=12, bold=True, color=NAVY)
    # Data cols
    for k, cell in enumerate(cells):
        box = add_shape_rect(s, col_x[k+1], y, col_widths[k+1], Inches(0.9), bg)
        box.line.color.rgb = RGBColor(0xDD, 0xDD, 0xDD)
        box.line.width = Pt(0.5)
        set_shape_text(box, cell, font_size=12, bold=False, color=DARK)

# ══════════════════════════════════════════════════════════════════════
# SLIDE 14: Kirkholt Project
# ══════════════════════════════════════════════════════════════════════
s = add_slide()
content_slide_header(s, "Policy Application: The Kirkholt Project")

items = [
    "Forrester, Chatterton & Pease (1988), Kirkholt estate, Rochdale, UK",
    "Problem: Extremely high burglary rates; repeat victimization common",
    "Intervention: Removed pre-payment gas/electricity meters (high-value targets in every home)",
    "Established \"cocoon neighbourhood watch\" \u2014 immediate neighbours of victims alerted",
    "Upgraded security for recently victimized households",
    "Result: 75% reduction in burglary over 3 years",
    "One of the most cited examples of situational crime prevention success",
]
add_bullet_list(s, items, font_size=17, spacing=10, width=Inches(8.0))

# Result highlight
box = add_rounded_rect(s, Inches(9.5), Inches(2.5), Inches(3.2), Inches(2.5), NAVY, GOLD)
tf_s = box.text_frame
tf_s.word_wrap = True
tf_s.vertical_anchor = MSO_ANCHOR.MIDDLE
p = tf_s.paragraphs[0]
p.text = "75%"
p.font.size = Pt(48)
p.font.bold = True
p.font.color.rgb = GOLD
p.font.name = FONT_TITLE
p.alignment = PP_ALIGN.CENTER
pp = tf_s.add_paragraph()
pp.text = "reduction in\nburglary"
pp.font.size = Pt(16)
pp.font.color.rgb = WHITE
pp.font.name = FONT_BODY
pp.alignment = PP_ALIGN.CENTER

# ══════════════════════════════════════════════════════════════════════
# SLIDE 15: Operation Ceasefire
# ══════════════════════════════════════════════════════════════════════
s = add_slide()
content_slide_header(s, "Policy Application: Operation Ceasefire")

items = [
    "Kennedy, Piehl & Braga (1997), Boston, Massachusetts",
    "Problem: Epidemic of youth gun violence; gang-related homicides",
    "\"Pulling levers\" strategy: directly communicating to gang members that violence would trigger a coordinated law enforcement response",
    "Combined deterrence (rational choice) with social service offers",
    "Interagency cooperation: police, probation, prosecutors, community workers",
    "Result: 63% reduction in youth homicide",
    "Replicated in multiple cities as the \"focused deterrence\" model",
]
add_bullet_list(s, items, font_size=17, spacing=10, width=Inches(8.0))

# Result highlight
box = add_rounded_rect(s, Inches(9.5), Inches(2.5), Inches(3.2), Inches(2.5), NAVY, GOLD)
tf_s = box.text_frame
tf_s.word_wrap = True
tf_s.vertical_anchor = MSO_ANCHOR.MIDDLE
p = tf_s.paragraphs[0]
p.text = "63%"
p.font.size = Pt(48)
p.font.bold = True
p.font.color.rgb = GOLD
p.font.name = FONT_TITLE
p.alignment = PP_ALIGN.CENTER
pp = tf_s.add_paragraph()
pp.text = "reduction in\nyouth homicide"
pp.font.size = Pt(16)
pp.font.color.rgb = WHITE
pp.font.name = FONT_BODY
pp.alignment = PP_ALIGN.CENTER

# ══════════════════════════════════════════════════════════════════════
# SLIDE 16: Criticisms
# ══════════════════════════════════════════════════════════════════════
s = add_slide()
content_slide_header(s, "Criticisms & Limitations")

criticisms = [
    ("Ignores root causes: Focuses on opportunity, not structural factors like poverty, inequality, and social exclusion", NAVY),
    ("Rationality assumption: Many crimes are impulsive, emotional, or committed under the influence of substances", RGBColor(0x8B, 0x3A, 0x3A)),
    ("Displacement concern: Prevention may simply move crime rather than reduce it (though evidence suggests otherwise)", RGBColor(0x6B, 0x3A, 0x2A)),
    ("Class and race blind: Target hardening may disproportionately protect affluent areas; surveillance may over-police minority communities", RGBColor(0x4A, 0x3A, 0x6A)),
    ("Theoretical narrowness: Cannot explain why some people are motivated to offend in the first place", RGBColor(0x3D, 0x5A, 0x3D)),
]

for i, (text, clr) in enumerate(criticisms):
    y = Inches(1.7) + i * Inches(1.05)
    # Color accent bar
    add_shape_rect(s, Inches(0.8), y, Inches(0.12), Inches(0.85), clr)
    # Text
    add_textbox(s, Inches(1.15), y + Inches(0.08), Inches(11.0), Inches(0.8),
                text, font_size=16, color=DARK)

# ══════════════════════════════════════════════════════════════════════
# SLIDE 17: Legacy & Significance
# ══════════════════════════════════════════════════════════════════════
s = add_slide()
content_slide_header(s, "Legacy & Significance")

items = [
    "Shifted criminology's central question from \"Why are criminals?\" to \"Why does crime happen here and now?\"",
    "Foundation of modern environmental criminology and crime science",
    "Directly shaped evidence-based policing (CompStat, PredPol, hot spots policing)",
    "Influenced urban planning, architecture (CPTED), and public space design",
    "Produced the most actionable, policy-relevant body of criminological research",
    "Demonstrated that crime can be reduced without solving \"root causes\"",
]
add_bullet_list(s, items, font_size=18, spacing=12)

# ══════════════════════════════════════════════════════════════════════
# SLIDE 18: Summary & Key Takeaways
# ══════════════════════════════════════════════════════════════════════
s = add_slide()
fill_bg(s, NAVY)
# Header
add_textbox(s, Inches(0.8), Inches(0.6), Inches(11.5), Inches(0.8),
            "Summary & Key Takeaways",
            font_size=32, bold=True, color=WHITE, alignment=PP_ALIGN.CENTER, font_name=FONT_TITLE)
add_gold_line(s, Inches(3.0), Inches(1.4), Inches(7.3), Pt(2))

takeaways = [
    "Rational Choice Theory: Offenders make bounded-rational decisions by weighing costs and benefits in specific situations.",
    "Routine Activity Theory: Crime requires the convergence of a motivated offender, suitable target, and absence of a capable guardian.",
    "Both theories are opportunity-focused, shifting attention from offender pathology to the crime event itself.",
    "These frameworks have produced highly effective, evidence-based policies: hot spots policing, situational prevention, focused deterrence.",
]

txBox = s.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(10.9), Inches(4.5))
tf = txBox.text_frame
tf.word_wrap = True
for i, item in enumerate(takeaways):
    p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
    # Number
    run1 = p.add_run()
    run1.text = f"{i+1}.  "
    run1.font.size = Pt(20)
    run1.font.bold = True
    run1.font.color.rgb = GOLD
    run1.font.name = FONT_TITLE
    # Text
    run2 = p.add_run()
    run2.text = item
    run2.font.size = Pt(18)
    run2.font.color.rgb = WHITE
    run2.font.name = FONT_BODY
    p.space_after = Pt(16)
    p.line_spacing = Pt(24)

# Bottom
add_gold_line(s, Inches(3.0), Inches(6.2), Inches(7.3), Pt(2))
add_textbox(s, Inches(0.8), Inches(6.4), Inches(11.5), Inches(0.5),
            "\"Opportunity makes the thief.\"  \u2014 Felson & Clarke (1998)",
            font_size=16, bold=False, color=GOLD, alignment=PP_ALIGN.CENTER)

add_slide_number(s, slide_number_counter[0], GOLD)

# ══════════════════════════════════════════════════════════════════════
# Save
# ══════════════════════════════════════════════════════════════════════
output_path = r"E:\권준성\lecture\ppt_rational_choice_routine_activity.pptx"
prs.save(output_path)
print(f"Presentation saved to: {output_path}")
print(f"Total slides: {len(prs.slides)}")
