#!/usr/bin/env python3
import json, re
from pathlib import Path
root=Path(__file__).resolve().parents[1]
assert (root/'index.html').exists()
assert 'current/in6/index.html' in (root/'index.html').read_text(encoding='utf-8')
assert (root/'current/in6/index.html').exists()
hero=root/'current/assets/brand/in6-hero.png'
assert hero.exists(), hero
assert hero.read_bytes().startswith(b'\x89PNG\r\n\x1a\n'), 'IN-6 hero is not a PNG'
entries=json.loads((root/'current/data/current_entries.json').read_text(encoding='utf-8'))
in6=[x for x in entries if x.get('scope')=='in6']
assert len(in6)==4, len(in6)
assert (root/'archive').exists(), 'legacy archive directory missing'
for row in in6:
    pack=root/'current/artifacts/entries'/f"{row['id']}.zip"
    assert pack.exists(), pack
print(json.dumps({'status':'PASS','current_in6_entries':len(in6),'legacy_archive_present':True},indent=2))
