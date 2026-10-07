"""Validate evidence linkage; does not certify content quality."""
import hashlib
import json
from pathlib import Path
import sys

def validate(content_path, review_path):
    content_path, review_path = Path(content_path), Path(review_path)
    raw = content_path.read_bytes()
    content, review = json.loads(raw), json.loads(review_path.read_bytes())
    errors = []
    if hashlib.sha256(raw).hexdigest() != review.get('content_sha256'):
        errors.append('content SHA-256 mismatch')
    slides, pages = content['slides'], review['pages']
    ids, rids = [s['id'] for s in slides], [p['id'] for p in pages]
    if len(ids) != len(set(ids)) or len(rids) != len(set(rids)):
        errors.append('duplicate page IDs')
    if ids != rids:
        errors.append('page coverage/order mismatch')
    mapping = {s['id']: s for s in slides}
    required = ['screen_answer', 'script_reason', 'previous_connection',
                'next_connection', 'initial_issue', 'resolution', 'final_check']
    for p in pages:
        s = mapping.get(p['id'])
        if s is None:
            continue
        for key in required:
            if not isinstance(p.get(key), str) or not p[key].strip():
                errors.append(f'{p["id"]}: missing {key}')
        screen = '\n'.join([s['title'], s['band'], s.get('context', ''),
                            *s['headers'], *[x for row in s['rows'] for x in row],
                            *s['below']])
        for key, text in [('screen_quote', screen), ('script_quote', '\n'.join(s['script']))]:
            if not isinstance(p.get(key), str) or not p[key].strip() or p[key] not in text:
                errors.append(f'{p["id"]}: ungrounded {key}')
        if p.get('status') not in ['PASS', 'HOLD', 'UNREVIEWED']:
            errors.append(f'{p["id"]}: invalid status')
        if not isinstance(p.get('open_issues'), list):
            errors.append(f'{p["id"]}: missing open_issues')
        elif p['status'] == 'PASS' and p['open_issues']:
            errors.append(f'{p["id"]}: PASS with open issues')
    for a in review.get('artifacts', []):
        path = review_path.parent / a['path']
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != a['sha256']:
            errors.append(f'artifact mismatch: {a["path"]}')
    return errors

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit('Usage: check_content_review.py CONTENT.json REVIEW.json')
    errors = validate(*sys.argv[1:])
    if errors:
        print('\n'.join(errors))
        raise SystemExit(1)
    print('Evidence linkage valid. Semantic and visual review remain manual.')
