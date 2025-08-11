#!/usr/bin/env python3
import hashlib, sys, pathlib
root = pathlib.Path('.')
paths = []
for p in root.rglob('*'):
    if p.is_file() and 'RELEASES' not in p.parts and '.git' not in p.parts:
        paths.append(p)
for p in sorted(paths):
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    print(f"{h}  {p}")
