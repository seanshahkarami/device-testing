#!/usr/bin/env python3
import re
import json
import sys

with open(sys.argv[1]) as f:
    firmware = eval(f.readline()).decode()
    config = eval(f.readline())
    body = f.read()


samples = []
blocks = list(map(str.strip, re.split('---', body)))

for values in blocks[1::2]:
    try:
        sample = dict((m.group(1), eval(m.group(2)))
                      for m in re.finditer('(.*)\s*:\s*(.*)', values))
    except SyntaxError:
        continue

    sample['timestamp'] = sample['Time']
    samples.append(sample)

print(json.dumps({
    'firmware': firmware,
    'config': config,
    'samples': samples
}))
