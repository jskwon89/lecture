# -*- coding: utf-8 -*-
"""행을 본문 영역(남색 선 ~ 마지막 구분선)에 고르게 배치한다.

행 높이는 실측한 내용 높이로 고정하고, 남는 공간은 모든 행에 같은 크기의
위·아래 여백으로만 쓴다. 행마다 여백이 달라지지 않으므로 늘어나 보이지 않고,
마지막 구분선이 늘 같은 자리(6.72)에 오므로 각주 위가 비지 않는다.
"""
from pptlib import (sp_text, sp_line, para, run, NAVY, INK, SUB, GOLD, LINE,
                    M_L, M_W, HEAD_X, HEAD_W, BODY_X, BODY_W)
from rowfit import n_lines, lh, SPC_AFT

LAST_RULE = 6.72          # 각주(7.02) 위에 두는 마지막 구분선
PAD_MIN, PAD_MAX = 0.11, 0.30
INK_FIX = 0.025           # 행머리글 잉크 중심 보정
BODY_FIX = 0.035          # 본문 글자 위쪽 내부 여백 보정


def _body_paras(conclusion, supplements, limit, csz, ss, bw, pgap=5):
    specs = [(conclusion, csz, INK, True)]
    specs += [(s, ss, SUB, False) for s in supplements]
    if limit:
        specs.append((limit, 12.0, GOLD, False))
    ps, h = [], 0.0
    for k, (s, pt, color, bold) in enumerate(specs):
        nl = n_lines(s, pt, bw, bold)
        pct = 125 if nl > 1 else 118
        last = (k == len(specs) - 1)
        ps.append(para([run(s, pt, color, bold=bold)],
                       lnspc=pct, spcaft=None if last else pgap))
        h += nl * lh(pt, pct) + (0 if last else pgap / 72.0)
    return ps, h


def layout_rows(next_id, y_rule, rows, close=None, gold=None, pgap=5,
                head_x=HEAD_X, head_w=HEAD_W, body_x=BODY_X, body_w=BODY_W,
                last_rule=LAST_RULE):
    """rows: (행머리글, 결론 줄, 보충 줄들[, 한정 줄]) 튜플의 목록
    close:  마지막 마무리 문장(구분선 두 개 사이)

    돌려주는 값: (도형 리스트, 다음 id, 마지막 구분선의 y)
    """
    sid = next_id
    blocks = []
    for r in rows:
        head, concl = r[0], r[1]
        supps = r[2] if len(r) > 2 else ()
        limit = r[3] if len(r) > 3 else None
        ps, bh = _body_paras(concl, supps, limit, 12.5, 11.5, body_w, pgap)
        hl = n_lines(head, 13.0, head_w, True)
        hpct = 125 if hl > 1 else 118
        blocks.append(dict(kind='row', head=head, hpct=hpct, ps=ps,
                           bh=bh, ch=max(bh, hl * lh(13.0, hpct))))
    if close:
        nl = n_lines(close, 12.5, M_W, True)
        blocks.append(dict(kind='close', text=close,
                           bh=nl * lh(12.5, 118), ch=nl * lh(12.5, 118)))
    if gold:
        nl = n_lines(gold, 12.0, M_W)
        blocks.append(dict(kind='gold', text=gold,
                           bh=nl * lh(12.0, 118), ch=nl * lh(12.0, 118)))

    n = len(blocks)
    total = sum(b['ch'] for b in blocks)
    pad = (last_rule - y_rule - total) / (2 * n)
    pad = max(PAD_MIN, min(PAD_MAX, pad))

    out, y = [], y_rule
    for k, b in enumerate(blocks):
        band_h = pad + b['ch'] + pad
        if b['kind'] == 'row':
            out.append(sp_text(sid, f'BODY{sid}', body_x, y + pad - BODY_FIX, body_w,
                               b['bh'], b['ps'], anchor='t')); sid += 1
            out.append(sp_text(sid, f'HEAD{sid}', head_x, y - INK_FIX, head_w, band_h,
                               [para([run(b['head'], 13.0, NAVY, bold=True)],
                                     align='ctr', lnspc=b['hpct'])],
                               anchor='ctr')); sid += 1
        elif b['kind'] == 'close':
            out.append(sp_text(sid, f'CLOSE{sid}', M_L, y + pad - BODY_FIX, M_W, b['bh'],
                               [para([run(b['text'], 12.5, INK, bold=True)],
                                     lnspc=118)], anchor='t')); sid += 1
        else:
            out.append(sp_text(sid, f'GOLD{sid}', M_L, y + pad - BODY_FIX, M_W, b['bh'],
                               [para([run(b['text'], 12.0, GOLD)], lnspc=118)],
                               anchor='t')); sid += 1
        y += band_h
        if k < n - 1 or close or gold:
            out.append(sp_line(sid, f'RULE{sid}', M_L, y, M_W, LINE, 0.75)); sid += 1
    return out, sid, y