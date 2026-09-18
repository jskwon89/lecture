# -*- coding: utf-8 -*-
"""Pretendard 실측으로 줄 수를 세어 행 높이를 정확히 잡는 보조 모듈.

pptlib.row()는 글자 수를 어림해 줄 수를 추정하므로, 실제 렌더 결과와
어긋나면 행마다 남는 공간이 달라져 구분선 사이 위·아래 여백이 틀어진다.
여기서는 실제 폰트 메트릭으로 줄바꿈을 계산해 상자 높이를 내용에 맞춘다.
"""
from PIL import ImageFont
from pptlib import (sp_text, sp_line, para, run, NAVY, INK, SUB, GOLD, LINE,
                    M_L, M_W, HEAD_X, HEAD_W, BODY_X, BODY_W)

_SCALE = 4          # 측정 정밀도를 위한 확대 배수
_cache = {}

def _font(pt, bold):
    key = (round(pt, 2), bold)
    if key not in _cache:
        path = '/root/.fonts/Pretendard-%s.ttf' % ('Bold' if bold else 'Regular')
        _cache[key] = ImageFont.truetype(path, int(round(pt * 96 / 72 * _SCALE)))
    return _cache[key]

def text_w(s, pt, bold=False):
    """문자열의 폭(인치)"""
    return _font(pt, bold).getlength(s) / _SCALE / 96.0

def n_lines(s, pt, box_w, bold=False):
    """상자 폭 안에서 실제로 몇 줄이 되는지 센다(어절 단위 줄바꿈, 한글은 글자 단위 허용)."""
    if not s:
        return 1
    f = _font(pt, bold)
    limit = box_w * 96 * _SCALE
    lines, cur = 1, 0.0
    token, tok_w = '', 0.0

    def flush():
        nonlocal lines, cur, token, tok_w
        if not token:
            return
        if cur > 0 and cur + tok_w > limit:
            lines += 1
            cur = tok_w
        else:
            cur += tok_w
        token, tok_w = '', 0.0

    for ch in s:
        w = f.getlength(ch)
        if ch == ' ':
            token += ch; tok_w += w
            flush()
            continue
        # 한글·한자·기호는 글자 단위로 줄바꿈된다
        if ord(ch) > 0x2000:
            flush()
            if cur > 0 and cur + w > limit:
                lines += 1; cur = w
            else:
                cur += w
        else:
            token += ch; tok_w += w
    flush()
    return lines

def lh(pt, pct):
    """한 줄의 높이(인치) — PowerPoint 기준 1.2 × 글자크기 × 줄간격"""
    return 1.2 * pt * (pct / 100.0) / 72.0

# 글자는 상자 위쪽에 내부 여백(leading)이 더 붙으므로, 실제 렌더에서
# 구분선과 글자 사이 간격이 위아래 같아지도록 위 여백을 조금 줄여 잡는다.
PAD_T = 0.105
PAD_B = 0.155
PAD = PAD_T + PAD_B
SPC_AFT = 5 / 72.0  # 문단 사이 간격 5pt


def row2(next_id, y, head, conclusion, supplements=(), limit=None,
         result=False, head_x=None, head_w=None, body_x=None, body_w=None,
         rule=True, cs=None, ss=11.5, band_top=None):
    """행머리글과 본문을 각각 자기 내용 높이에 맞춘 상자로 만들고,
    구분선 사이의 위·아래 여백을 같은 값(PAD)으로 맞춘다.

    돌려주는 값: (도형 리스트, 다음 id, 다음 구분선의 y)
    """
    sid = next_id
    hx = HEAD_X if head_x is None else head_x
    hw = HEAD_W if head_w is None else head_w
    bx = BODY_X if body_x is None else body_x
    bw = BODY_W if body_w is None else body_w
    out = []
    if rule:
        out.append(sp_line(sid, f'RULE{sid}', M_L, y, M_W, LINE, 0.75)); sid += 1

    csz = cs if cs else (13.0 if result else 12.5)

    # ── 본문 문단 구성과 실제 높이 계산 ───────────────────────
    specs = [(conclusion, csz, INK, True)]
    specs += [(s, ss, SUB, False) for s in supplements]
    if limit:
        specs.append((limit, 12.0, GOLD, False))

    ps, body_h = [], 0.0
    for k, (s, pt, color, bold) in enumerate(specs):
        nl = n_lines(s, pt, bw, bold)
        pct = 125 if nl > 1 else 118
        last = (k == len(specs) - 1)
        ps.append(para([run(s, pt, color, bold=bold)],
                       lnspc=pct, spcaft=None if last else 5))
        body_h += nl * lh(pt, pct) + (0 if last else SPC_AFT)

    # ── 본문은 위쪽 기준, 행머리글은 행 전체의 한가운데 ──────────
    hl = n_lines(head, 13.0, hw, True)
    hpct = 125 if hl > 1 else 118
    head_h = hl * lh(13.0, hpct)

    out.append(sp_text(sid, f'BODY{sid}', bx, y + PAD_T, bw, body_h, ps,
                       anchor='t')); sid += 1

    # 행머리글은 구분선과 구분선 사이의 한가운데에 둔다.
    # 글자의 잉크 중심이 상자 중심보다 조금 아래에 맺히므로 0.025인치 올려 잡는다.
    bt = y if band_top is None else band_top
    band_h = (y + PAD_T + max(head_h, body_h) + PAD_B) - bt
    out.append(sp_text(sid, f'HEAD{sid}', hx, bt - 0.025, hw, band_h,
                       [para([run(head, 13.0, NAVY, bold=True)],
                             align='ctr', lnspc=hpct)],
                       anchor='ctr')); sid += 1

    content_h = max(head_h, body_h)
    return out, sid, y + PAD_T + content_h + PAD_B