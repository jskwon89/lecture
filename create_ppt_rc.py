# -*- coding: utf-8 -*-
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
import copy

# Constants
SLIDE_W = 9144000
SLIDE_H = 5143500

# Colors
TEAL = RGBColor(0x1B, 0x7A, 0x6E)
NAVY = RGBColor(0x2D, 0x3E, 0x5F)
DARK_NAVY = RGBColor(0x1E, 0x2D, 0x4A)
TEXT_DARK = RGBColor(0x22, 0x22, 0x22)
TEXT_GRAY = RGBColor(0x66, 0x66, 0x66)
SUBTITLE_BLUE = RGBColor(0x88, 0x99, 0xBB)
NAME_COLOR = RGBColor(0xAA, 0xBB, 0xCC)
RED = RGBColor(0xC0, 0x39, 0x2B)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
MINT_BG = RGBColor(0xE8, 0xF5, 0xF2)
GRAY_BG = RGBColor(0xF5, 0xF6, 0xFA)
BLUE_BG = RGBColor(0xE3, 0xF0, 0xFC)
RED_BG = RGBColor(0xFF, 0xF5, 0xF5)

prs = Presentation()
prs.slide_width = SLIDE_W
prs.slide_height = SLIDE_H

# Use blank layout
blank_layout = prs.slide_layouts[6]  # blank


def set_slide_bg(slide, color):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_shape(slide, left, top, width, height, fill_color=None, shape_type=MSO_SHAPE.RECTANGLE):
    shape = slide.shapes.add_shape(shape_type, left, top, width, height)
    shape.line.fill.background()
    if fill_color:
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill_color
    else:
        shape.fill.background()
    return shape


def add_rounded_rect(slide, left, top, width, height, fill_color=None):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.line.fill.background()
    if fill_color:
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill_color
    else:
        shape.fill.background()
    # Adjust corner radius
    shape.adjustments[0] = 0.1
    return shape


def add_textbox(slide, left, top, width, height):
    txBox = slide.shapes.add_textbox(left, top, width, height)
    return txBox


def add_text_shape(slide, left, top, width, height, text, font_name="Calibri", font_size=16, bold=False, color=TEXT_DARK, alignment=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    txBox = add_textbox(slide, left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    tf.auto_size = None
    p = tf.paragraphs[0]
    p.alignment = alignment
    run = p.add_run()
    run.text = text
    run.font.name = font_name
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.color.rgb = color
    tf.paragraphs[0].space_before = Pt(0)
    tf.paragraphs[0].space_after = Pt(0)
    return txBox


def add_part_label(slide, text, left=457200, top=164592):
    """Add PART label - teal rounded rect with white text"""
    shape = add_rounded_rect(slide, left, top, 2377440, 274320, TEAL)
    shape.text_frame.word_wrap = False
    p = shape.text_frame.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = text
    run.font.name = "Calibri"
    run.font.size = Pt(11)
    run.font.bold = True
    run.font.color.rgb = WHITE
    shape.text_frame.paragraphs[0].space_before = Pt(0)
    shape.text_frame.paragraphs[0].space_after = Pt(0)
    return shape


def add_slide_title(slide, text, top=594360, font_size=26):
    """Add Georgia Bold title"""
    return add_text_shape(slide, 457200, top, 8229600, 502920, text,
                          font_name="Georgia", font_size=font_size, bold=True, color=TEXT_DARK)


def add_subtitle(slide, text, top=1051560):
    return add_text_shape(slide, 457200, top, 3657600, 274320, text,
                          font_name="Calibri", font_size=14, color=TEXT_GRAY)


def add_numbered_circle(slide, number, cx, cy, radius=205740):
    """Add a teal circle with white number centered at (cx, cy)"""
    shape = slide.shapes.add_shape(MSO_SHAPE.OVAL, cx - radius, cy - radius, radius * 2, radius * 2)
    shape.line.fill.background()
    shape.fill.solid()
    shape.fill.fore_color.rgb = TEAL
    tf = shape.text_frame
    tf.word_wrap = False
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = str(number)
    run.font.name = "Calibri"
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.color.rgb = WHITE
    shape.text_frame.paragraphs[0].space_before = Pt(0)
    shape.text_frame.paragraphs[0].space_after = Pt(0)
    return shape


def add_box_with_text(slide, left, top, width, height, text, fill_color=MINT_BG, text_color=TEXT_DARK, font_size=13, bold=False, alignment=PP_ALIGN.CENTER, border_color=None):
    shape = add_rounded_rect(slide, left, top, width, height, fill_color)
    if border_color:
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1)
    tf = shape.text_frame
    tf.word_wrap = True
    tf.auto_size = None
    p = tf.paragraphs[0]
    p.alignment = alignment
    run = p.add_run()
    run.text = text
    run.font.name = "Calibri"
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.color.rgb = text_color
    p.space_before = Pt(2)
    p.space_after = Pt(2)
    return shape


def add_limitation_box(slide, left, top, width, height, text, font_size=12):
    """Light red box with red accent bar on left"""
    shape = add_shape(slide, left, top, width, height, RED_BG)
    # Red accent bar
    bar = add_shape(slide, left, top, 53975, height, RED)
    # Text
    add_text_shape(slide, left + 80000, top + 30000, width - 100000, height - 60000, text,
                   font_size=font_size, color=TEXT_DARK)
    return shape


# ==================== SLIDE 1: Title ====================
slide1 = prs.slides.add_slide(blank_layout)
set_slide_bg(slide1, NAVY)

# Title lines
add_text_shape(slide1, 731520, 457200, 7315200, 1280160, "Rational Choice",
               font_name="Georgia", font_size=52, bold=True, color=WHITE)
add_text_shape(slide1, 731520, 1371600, 7315200, 1280160, "& Routine Activity Theory",
               font_name="Georgia", font_size=52, bold=True, color=WHITE)

# Subtitle
add_text_shape(slide1, 731520, 3017520, 7315200, 457200,
               "Cornish & Clarke; Cohen & Felson (1970s-80s)",
               font_name="Calibri", font_size=17, color=SUBTITLE_BLUE)

# Divider line
line_shape = add_shape(slide1, 731520, 3749040, 2286000, 18000, SUBTITLE_BLUE)

# Presenter name
add_text_shape(slide1, 731520, 4023360, 1609535, 365760, "Kwon Joon-sung",
               font_name="Calibri", font_size=14, bold=True, color=NAME_COLOR)


# ==================== SLIDE 2: Overview ====================
slide2 = prs.slides.add_slide(blank_layout)
set_slide_bg(slide2, WHITE)

add_text_shape(slide2, 457200, 137160, 2743200, 274320, "OVERVIEW",
               font_name="Calibri", font_size=14, bold=True, color=TEXT_GRAY)

add_slide_title(slide2, "Rational Choice & Routine Activity Theory", top=457200, font_size=26)

# Key Point box
kp_box = add_shape(slide2, 457200, 1188720, 8229600, 731520, MINT_BG)
txBox = add_textbox(slide2, 520000, 1250000, 8100000, 600000)
tf = txBox.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
run1 = p.add_run()
run1.text = "Key Point: "
run1.font.name = "Calibri"
run1.font.size = Pt(15)
run1.font.bold = True
run1.font.color.rgb = TEAL
run2 = p.add_run()
run2.text = "Offenders make rational decisions; crime occurs when opportunity meets motivation."
run2.font.name = "Calibri"
run2.font.size = Pt(15)
run2.font.color.rgb = TEXT_DARK

# Theory section boxes (teal)
theory_boxes = [
    ("Rational\nChoice", 457200),
    ("Routine\nActivity", 2103120),
    ("Crime\nTriangle", 3749040),
]
for text, left in theory_boxes:
    add_box_with_text(slide2, left, 2300000, 1554480, 914400, text,
                      fill_color=TEAL, text_color=WHITE, font_size=14, bold=True)

# Arrows between theory boxes
add_text_shape(slide2, 2011608, 2500000, 91440, 500000, "\u2192",
               font_size=20, bold=True, color=TEXT_GRAY, alignment=PP_ALIGN.CENTER)
add_text_shape(slide2, 3657600, 2500000, 91440, 500000, "\u2192",
               font_size=20, bold=True, color=TEXT_GRAY, alignment=PP_ALIGN.CENTER)

# Arrow to practice
add_text_shape(slide2, 5303520, 2500000, 274320, 500000, "\u2192",
               font_size=20, bold=True, color=TEXT_GRAY, alignment=PP_ALIGN.CENTER)

# Practice section boxes (navy)
add_box_with_text(slide2, 5715000, 2300000, 1280160, 914400, "Hot Spots\nPolicing",
                  fill_color=NAVY, text_color=WHITE, font_size=14, bold=True)
add_text_shape(slide2, 6995160, 2500000, 274320, 500000, "&",
               font_size=16, bold=True, color=TEXT_GRAY, alignment=PP_ALIGN.CENTER)
add_box_with_text(slide2, 7269480, 2300000, 1280160, 914400, "SCP",
                  fill_color=NAVY, text_color=WHITE, font_size=16, bold=True)

# Bottom text
add_text_shape(slide2, 457200, 4224788, 8229600, 365760,
               "Research: Empirical Evidence & Policy Applications",
               font_name="Calibri", font_size=14, bold=True, color=TEXT_GRAY)


# ==================== SLIDE 3: Rational Choice Theory ====================
slide3 = prs.slides.add_slide(blank_layout)
set_slide_bg(slide3, WHITE)

add_part_label(slide3, "PART 1 \u2014 THEORY")
add_slide_title(slide3, "Rational Choice Theory")
add_subtitle(slide3, "Cornish & Clarke, 1986")

# Box 1: Classical Roots
add_shape(slide3, 457200, 1463040, 8229600, 640080, GRAY_BG)
txBox = add_textbox(slide3, 520000, 1480000, 8100000, 600000)
tf = txBox.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
r = p.add_run()
r.text = "Classical Roots: "
r.font.name = "Calibri"; r.font.size = Pt(14); r.font.bold = True; r.font.color.rgb = TEAL
r2 = p.add_run()
r2.text = "Beccaria & Bentham \u2014 offenders as rational actors who calculate pleasure vs pain"
r2.font.name = "Calibri"; r2.font.size = Pt(14); r2.font.color.rgb = TEXT_DARK

# Box 2: Core Premise
add_shape(slide3, 457200, 2194560, 8229600, 640080, BLUE_BG)
txBox = add_textbox(slide3, 520000, 2210000, 8100000, 600000)
tf = txBox.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
r = p.add_run()
r.text = "Core Premise: "
r.font.name = "Calibri"; r.font.size = Pt(14); r.font.bold = True; r.font.color.rgb = TEAL
r2 = p.add_run()
r2.text = "Offenders weigh costs vs benefits before committing crime"
r2.font.name = "Calibri"; r2.font.size = Pt(14); r2.font.color.rgb = TEXT_DARK

# Bounded Rationality insight
add_shape(slide3, 457200, 2926080, 8229600, 502920, MINT_BG)
txBox = add_textbox(slide3, 520000, 2940000, 8100000, 460000)
tf = txBox.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
r = p.add_run()
r.text = "Bounded Rationality (Herbert Simon): "
r.font.name = "Calibri"; r.font.size = Pt(14); r.font.bold = True; r.font.color.rgb = TEAL
r2 = p.add_run()
r2.text = "Not perfectly rational, but reasoning within cognitive and informational limits"
r2.font.name = "Calibri"; r2.font.size = Pt(14); r2.font.color.rgb = TEXT_DARK

# Decision types - two side by side boxes
add_box_with_text(slide3, 457200, 3657600, 3840480, 731520,
                  "Involvement Decisions\n(start / continue / stop offending)",
                  fill_color=TEAL, text_color=WHITE, font_size=14, bold=True)
add_box_with_text(slide3, 4846320, 3657600, 3840480, 731520,
                  "Event Decisions\n(when / where / how to commit)",
                  fill_color=TEAL, text_color=WHITE, font_size=14, bold=True)


# ==================== SLIDE 4: Routine Activity Theory ====================
slide4 = prs.slides.add_slide(blank_layout)
set_slide_bg(slide4, WHITE)

add_part_label(slide4, "PART 1 \u2014 THEORY")
add_slide_title(slide4, "Three Minimal Elements for Crime")
add_subtitle(slide4, "Cohen & Felson, 1979")

# Three numbered circles with boxes
elements = [
    (1, 1884489, "Motivated\nOffender"),
    (2, 4458723, "Suitable\nTarget"),
    (3, 6914328, "Absence of\nCapable Guardian"),
]

for num, cx, text in elements:
    add_numbered_circle(slide4, num, cx, 1290328 + 205740)
    box_left = cx - 855000
    fill = TEAL if num <= 2 else GRAY_BG
    txt_color = WHITE if num <= 2 else TEAL
    brd = TEAL if num == 3 else None
    shape = add_box_with_text(slide4, box_left, 1886659, 1710000, 640080, text,
                              fill_color=fill, text_color=txt_color, font_size=14, bold=True,
                              border_color=brd)

# Plus signs
add_text_shape(slide4, 2639489, 1950000, 500000, 500000, "+",
               font_size=24, bold=True, color=TEXT_GRAY, alignment=PP_ALIGN.CENTER)
add_text_shape(slide4, 5213723, 1950000, 500000, 500000, "+",
               font_size=24, bold=True, color=TEXT_GRAY, alignment=PP_ALIGN.CENTER)

# Convergence text
add_box_with_text(slide4, 2205228, 2709080, 4572000, 347980,
                  "Convergence in space and time",
                  fill_color=GRAY_BG, text_color=TEAL, font_size=14, bold=True)

# Result boxes
eq_shape = slide4.shapes.add_shape(MSO_SHAPE.RECTANGLE, 806849, 3359150, 381000, 320040)
eq_shape.fill.solid(); eq_shape.fill.fore_color.rgb = TEAL; eq_shape.line.fill.background()
eq_tf = eq_shape.text_frame; eq_p = eq_tf.paragraphs[0]; eq_p.alignment = PP_ALIGN.CENTER
eq_r = eq_p.add_run(); eq_r.text = "="; eq_r.font.name = "Calibri"; eq_r.font.size = Pt(16)
eq_r.font.bold = True; eq_r.font.color.rgb = WHITE

add_box_with_text(slide4, 1237379, 3338830, 2477670, 365760, "Crime occurs",
                  fill_color=TEAL, text_color=WHITE, font_size=14, bold=True)

add_text_shape(slide4, 3788315, 3336290, 170127, 365760, "&",
               font_size=14, bold=True, color=TEXT_GRAY, alignment=PP_ALIGN.CENTER)

add_box_with_text(slide4, 4031709, 3338830, 4014832, 368009,
                  "Lack of any one \u2192 sufficient to prevent crime",
                  fill_color=GRAY_BG, text_color=TEXT_DARK, font_size=13, bold=False)

# Limitation box
add_limitation_box(slide4, 596900, 4069286, 8096250, 612902,
                   "Limitation: Takes criminal inclination as given \u2014 does not explain HOW offender becomes motivated")


# ==================== SLIDE 5: VIVA & Crime Triangle ====================
slide5 = prs.slides.add_slide(blank_layout)
set_slide_bg(slide5, WHITE)

add_part_label(slide5, "PART 1 \u2014 THEORY")
add_slide_title(slide5, "VIVA  & Crime Triangle", font_size=26)

# Left side - VIVA
add_text_shape(slide5, 457200, 1100000, 3840480, 274320,
               "VIVA Criteria \u2014 Cohen & Felson, 1979",
               font_name="Calibri", font_size=13, bold=True, color=TEXT_GRAY)

viva_items = [
    ("V", "alue \u2014 Material or symbolic desirability of target"),
    ("I", "nertia \u2014 Weight, size, portability"),
    ("V", "isibility \u2014 Exposure to offenders"),
    ("A", "ccess \u2014 How easy to reach"),
]

y_start = 1500000
for i, (letter, desc) in enumerate(viva_items):
    y = y_start + i * 400000
    # Teal circle for letter
    circle = slide5.shapes.add_shape(MSO_SHAPE.OVAL, 457200, y, 292608, 329184)
    circle.line.fill.background()
    circle.fill.solid(); circle.fill.fore_color.rgb = TEAL
    tf = circle.text_frame; p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = letter; r.font.name = "Calibri"; r.font.size = Pt(14)
    r.font.bold = True; r.font.color.rgb = WHITE

    add_text_shape(slide5, 868680, y, 3525074, 329184, desc,
                   font_size=13, color=TEXT_DARK)

# Example box
add_box_with_text(slide5, 457200, 3200000, 3840480, 400000,
                  "E.g.) Phone on a caf\u00e9 table = near-perfect target",
                  fill_color=MINT_BG, text_color=TEXT_DARK, font_size=12, bold=False,
                  alignment=PP_ALIGN.LEFT)

# Right side - Crime Triangle
add_text_shape(slide5, 5100000, 1100000, 3500000, 274320,
               "Crime Triangle \u2014 Eck, 2003",
               font_name="Calibri", font_size=13, bold=True, color=TEXT_GRAY)

# Inner triangle labels
inner_labels = [
    ("Offender", 6400000, 1550000),
    ("Target", 5400000, 2900000),
    ("Place", 7400000, 2900000),
]

for text, x, y in inner_labels:
    box = add_box_with_text(slide5, x, y, 1100000, 350000, text,
                            fill_color=TEAL, text_color=WHITE, font_size=12, bold=True)

# Outer triangle labels
outer_labels = [
    ("Handler", 5100000, 1550000, "(e.g. parent, friend)"),
    ("Guardian", 5100000, 3350000, "(e.g. ordinary citizen)"),
    ("Manager", 7200000, 3350000, "(e.g. owner, staff)"),
]

for text, x, y, example in outer_labels:
    add_text_shape(slide5, x, y, 1200000, 250000, text,
                   font_size=11, bold=True, color=NAVY)
    add_text_shape(slide5, x, y + 220000, 1200000, 200000, example,
                   font_size=9, color=TEXT_GRAY)

# Control text
add_text_shape(slide5, 5400000, 4000000, 3800000, 350000,
               "If any one controller functions = crime can be prevented",
               font_size=11, bold=True, color=TEAL)


# ==================== SLIDE 6: Situational Crime Prevention ====================
slide6 = prs.slides.add_slide(blank_layout)
set_slide_bg(slide6, WHITE)

add_part_label(slide6, "PART 1 \u2014 THEORY")
add_slide_title(slide6, "Situational Crime Prevention (SCP)")

# SCP subtitle box
add_box_with_text(slide6, 457200, 1171202, 8296910, 500000,
                  "Clarke (1992) \u2192 Cornish & Clarke (2003): 25 Techniques in 5 Categories",
                  fill_color=TEAL, text_color=WHITE, font_size=13, bold=True)

# Five numbered strategies
strategies = [
    (1, "Increase\nEffort", "Target hardening,\naccess control"),
    (2, "Increase\nRisk", "Surveillance,\nCCTV, lighting"),
    (3, "Reduce\nRewards", "Remove targets,\nmark property"),
    (4, "Reduce\nProvocation", "Reduce frustration,\navoid disputes"),
    (5, "Remove\nExcuses", "Set rules,\npost instructions"),
]

for i, (num, title, example) in enumerate(strategies):
    cx = 883920 + i * 1737360
    # Numbered circle
    add_numbered_circle(slide6, num, cx, 2006092 + 205740)
    # Strategy box
    box_left = cx - 693420
    add_box_with_text(slide6, box_left, 2509012, 1386840, 640080, title,
                      fill_color=MINT_BG, text_color=TEXT_DARK, font_size=13, bold=True)
    # Example below
    add_text_shape(slide6, box_left, 3200000, 1386840, 500000, example,
                   font_size=10, color=TEXT_GRAY, alignment=PP_ALIGN.CENTER)

# Bottom examples row
add_box_with_text(slide6, 457200, 3900000, 8229600, 500000,
                  "Example: Steering column locks (Effort) | CCTV in parking garages (Risk) | Ink tags on clothing (Rewards)",
                  fill_color=GRAY_BG, text_color=TEXT_DARK, font_size=12, bold=False,
                  alignment=PP_ALIGN.LEFT)


# ==================== SLIDE 7: Hot Spots & Evidence ====================
slide7 = prs.slides.add_slide(blank_layout)
set_slide_bg(slide7, WHITE)

add_part_label(slide7, "PART 2 \u2014 RESEARCH")
add_slide_title(slide7, "Empirical Evidence")

# Box 1
add_shape(slide7, 457200, 1200000, 8229600, 780000, GRAY_BG)
txBox = add_textbox(slide7, 520000, 1220000, 8100000, 740000)
tf = txBox.text_frame; tf.word_wrap = True
p = tf.paragraphs[0]
r = p.add_run(); r.text = "Sherman, Gartin & Buerger (1989) \u2014 Minneapolis"; r.font.name = "Calibri"
r.font.size = Pt(14); r.font.bold = True; r.font.color.rgb = NAVY
p2 = tf.add_paragraph()
r2 = p2.add_run(); r2.text = "3.5% of addresses \u2192 50% of all police calls"
r2.font.name = "Calibri"; r2.font.size = Pt(13); r2.font.color.rgb = TEXT_DARK

# Box 2
add_shape(slide7, 457200, 2080000, 8229600, 780000, BLUE_BG)
txBox = add_textbox(slide7, 520000, 2100000, 8100000, 740000)
tf = txBox.text_frame; tf.word_wrap = True
p = tf.paragraphs[0]
r = p.add_run(); r.text = "Braga et al. (2014) \u2014 Meta-analysis of 25 studies"; r.font.name = "Calibri"
r.font.size = Pt(14); r.font.bold = True; r.font.color.rgb = NAVY
p2 = tf.add_paragraph()
r2 = p2.add_run(); r2.text = "Hot spots policing: significant crime reduction with little displacement"
r2.font.name = "Calibri"; r2.font.size = Pt(13); r2.font.color.rgb = TEXT_DARK

# Box 3
add_shape(slide7, 457200, 2960000, 8229600, 780000, MINT_BG)
txBox = add_textbox(slide7, 520000, 2980000, 8100000, 740000)
tf = txBox.text_frame; tf.word_wrap = True
p = tf.paragraphs[0]
r = p.add_run(); r.text = "Guerette & Bowers (2009) \u2014 102 evaluations"; r.font.name = "Calibri"
r.font.size = Pt(14); r.font.bold = True; r.font.color.rgb = NAVY
p2 = tf.add_paragraph()
r2 = p2.add_run(); r2.text = "Displacement: only 26% of studies | Diffusion of benefits: 27%"
r2.font.name = "Calibri"; r2.font.size = Pt(13); r2.font.color.rgb = TEXT_DARK

# Key insight
add_shape(slide7, 457200, 3900000, 8229600, 502920, MINT_BG)
txBox = add_textbox(slide7, 520000, 3920000, 8100000, 460000)
tf = txBox.text_frame; tf.word_wrap = True
p = tf.paragraphs[0]
r = p.add_run(); r.text = "Key Insight: "; r.font.name = "Calibri"; r.font.size = Pt(14)
r.font.bold = True; r.font.color.rgb = TEAL
r2 = p.add_run()
r2.text = "\"Crime does not simply move around the corner\" \u2014 Weisburd et al. (2006)"
r2.font.name = "Calibri"; r2.font.size = Pt(14); r2.font.color.rgb = TEXT_DARK


# ==================== SLIDE 8: Case Studies ====================
slide8 = prs.slides.add_slide(blank_layout)
set_slide_bg(slide8, WHITE)

add_part_label(slide8, "PART 2 \u2014 RESEARCH")
add_slide_title(slide8, "Policy Applications")

# Case 1
add_shape(slide8, 457200, 1200000, 8229600, 880000, MINT_BG)
txBox = add_textbox(slide8, 520000, 1220000, 8100000, 840000)
tf = txBox.text_frame; tf.word_wrap = True
p = tf.paragraphs[0]
r = p.add_run(); r.text = "Kirkholt Burglary Prevention \u2014 Forrester et al. (1988, UK)"
r.font.name = "Calibri"; r.font.size = Pt(14); r.font.bold = True; r.font.color.rgb = NAVY
p2 = tf.add_paragraph()
r2 = p2.add_run(); r2.text = "Removed gas meters (coin-operated) + cocoon neighbourhood watch"
r2.font.name = "Calibri"; r2.font.size = Pt(13); r2.font.color.rgb = TEXT_DARK
p3 = tf.add_paragraph()
r3 = p3.add_run(); r3.text = "\u2192 75% reduction in burglary"; r3.font.name = "Calibri"
r3.font.size = Pt(13); r3.font.bold = True; r3.font.color.rgb = TEAL

# Case 2
add_shape(slide8, 457200, 2200000, 8229600, 880000, BLUE_BG)
txBox = add_textbox(slide8, 520000, 2220000, 8100000, 840000)
tf = txBox.text_frame; tf.word_wrap = True
p = tf.paragraphs[0]
r = p.add_run(); r.text = "Operation Ceasefire \u2014 Kennedy (1997, Boston)"
r.font.name = "Calibri"; r.font.size = Pt(14); r.font.bold = True; r.font.color.rgb = NAVY
p2 = tf.add_paragraph()
r2 = p2.add_run(); r2.text = "Pulling levers: communicating consequences directly to gang members"
r2.font.name = "Calibri"; r2.font.size = Pt(13); r2.font.color.rgb = TEXT_DARK
p3 = tf.add_paragraph()
r3 = p3.add_run(); r3.text = "\u2192 63% reduction in youth homicide"; r3.font.name = "Calibri"
r3.font.size = Pt(13); r3.font.bold = True; r3.font.color.rgb = TEAL

# Case 3
add_shape(slide8, 457200, 3200000, 8229600, 880000, GRAY_BG)
txBox = add_textbox(slide8, 520000, 3220000, 8100000, 840000)
tf = txBox.text_frame; tf.word_wrap = True
p = tf.paragraphs[0]
r = p.add_run(); r.text = "Netherlands National Strategy \u2014 Webb (1994)"
r.font.name = "Calibri"; r.font.size = Pt(14); r.font.bold = True; r.font.color.rgb = NAVY
p2 = tf.add_paragraph()
r2 = p2.add_run(); r2.text = "Mandatory steering column locks on all new vehicles"
r2.font.name = "Calibri"; r2.font.size = Pt(13); r2.font.color.rgb = TEXT_DARK
p3 = tf.add_paragraph()
r3 = p3.add_run(); r3.text = "\u2192 50% reduction in car theft"; r3.font.name = "Calibri"
r3.font.size = Pt(13); r3.font.bold = True; r3.font.color.rgb = TEAL


# ==================== SLIDE 9: Criticisms & Comparisons ====================
slide9 = prs.slides.add_slide(blank_layout)
set_slide_bg(slide9, WHITE)

add_slide_title(slide9, "Criticisms & Comparisons", top=228600)

# Limitations section
add_text_shape(slide9, 457200, 800000, 4000000, 274320, "Limitations",
               font_name="Calibri", font_size=14, bold=True, color=RED)

limitations = [
    "Ignores root causes \u2014 poverty, inequality, social structure",
    "Assumes too much rationality \u2014 many crimes are impulsive or emotional",
    "Class and race blind \u2014 does not address structural disadvantage",
]

for i, lim in enumerate(limitations):
    y = 1100000 + i * 450000
    add_limitation_box(slide9, 457200, y, 8229600, 370000, lim, font_size=12)

# Comparison section
add_text_shape(slide9, 457200, 2600000, 4000000, 274320, "Theory Comparisons",
               font_name="Calibri", font_size=14, bold=True, color=TEAL)

# Header row
header_y = 2920000
add_box_with_text(slide9, 457200, header_y, 2700000, 350000, "Theory",
                  fill_color=TEAL, text_color=WHITE, font_size=12, bold=True)
add_box_with_text(slide9, 3257200, header_y, 2700000, 350000, "Core Question",
                  fill_color=TEAL, text_color=WHITE, font_size=12, bold=True)
add_box_with_text(slide9, 6057200, header_y, 2629600, 350000, "Focus",
                  fill_color=TEAL, text_color=WHITE, font_size=12, bold=True)

# Data rows
comparisons = [
    ("Rational Choice\n(Cornish & Clarke)", "When/where does\ncrime happen?", "Opportunity"),
    ("Social Bond\n(Hirschi)", "Why do people\nconform?", "Bonds"),
    ("General Strain\n(Agnew)", "Why do people\noffend?", "Pressure"),
]

for i, (theory, question, focus) in enumerate(comparisons):
    y = 3320000 + i * 500000
    bg = GRAY_BG if i % 2 == 0 else WHITE
    add_box_with_text(slide9, 457200, y, 2700000, 450000, theory,
                      fill_color=bg, text_color=TEXT_DARK, font_size=11, bold=True,
                      alignment=PP_ALIGN.LEFT)
    add_box_with_text(slide9, 3257200, y, 2700000, 450000, question,
                      fill_color=bg, text_color=TEXT_DARK, font_size=11,
                      alignment=PP_ALIGN.LEFT)
    add_box_with_text(slide9, 6057200, y, 2629600, 450000, focus,
                      fill_color=bg, text_color=TEAL, font_size=13, bold=True)


# ==================== SLIDE 10: Conclusion ====================
slide10 = prs.slides.add_slide(blank_layout)
set_slide_bg(slide10, WHITE)

add_slide_title(slide10, "Conclusion", top=228600)

# Summary box (dark navy)
add_shape(slide10, 409330, 937260, 8229600, 1371600, DARK_NAVY)
txBox = add_textbox(slide10, 637930, 1005840, 7772400, 1188720)
tf = txBox.text_frame; tf.word_wrap = True

lines = [
    ("Focus: ", "Opportunity structure (not offender pathology)"),
    ("Theory: ", "Rational Choice + Routine Activity + Crime Triangle"),
    ("Practice: ", "SCP, Hot Spots Policing, CPTED"),
    ("Evidence: ", "Strong empirical support across multiple studies"),
]

for i, (label, content) in enumerate(lines):
    if i == 0:
        p = tf.paragraphs[0]
    else:
        p = tf.add_paragraph()
    r1 = p.add_run(); r1.text = label; r1.font.name = "Calibri"; r1.font.size = Pt(14)
    r1.font.bold = True; r1.font.color.rgb = RGBColor(0x8B, 0xCF, 0xC1)
    r2 = p.add_run(); r2.text = content; r2.font.name = "Calibri"; r2.font.size = Pt(14)
    r2.font.color.rgb = WHITE
    p.space_before = Pt(4); p.space_after = Pt(4)

# Limitations header
add_text_shape(slide10, 457200, 2500000, 955093, 320040, "Limitations",
               font_name="Calibri", font_size=14, bold=True, color=TEXT_DARK)

# Limitation lines
lim_lines = [
    "1. Crime displacement \u2014 may relocate crime rather than eliminate it",
    "2. Takes offender motivation as given \u2014 does not address root causes",
    "3. Application to private / digital spaces remains limited",
]
for i, line in enumerate(lim_lines):
    add_text_shape(slide10, 731520, 2880000 + i * 300000, 7772400, 274320, line,
                   font_name="Calibri", font_size=13, color=TEXT_DARK)

# Divider line
add_shape(slide10, 351876, 3800000, 8229600, 18000, TEXT_GRAY)

# Bottom key message
txBox = add_textbox(slide10, 726732, 3900000, 7772400, 731519)
tf = txBox.text_frame; tf.word_wrap = True
p = tf.paragraphs[0]
r = p.add_run()
r.text = "No single approach is sufficient"
r.font.name = "Calibri"; r.font.size = Pt(16); r.font.bold = True; r.font.color.rgb = TEAL
p2 = tf.add_paragraph()
r2 = p2.add_run()
r2.text = "     \u2192 Comprehensive understanding based on diverse frameworks is essential."
r2.font.name = "Calibri"; r2.font.size = Pt(14); r2.font.bold = True; r2.font.color.rgb = TEXT_DARK


# Save
prs.save('ppt_rational_choice_routine_activity.pptx')
print("DONE: ppt_rational_choice_routine_activity.pptx created successfully")
