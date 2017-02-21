#!/usr/bin/env python3
from datetime import datetime
import re
import json
import sys

with open(sys.argv[1]) as f:
    firmware = eval(f.readline()).decode()
    config = eval(f.readline())
    body = f.read()


samples = []
blocks = list(map(str.strip, re.split('---', body)))

for timestamp, values in zip(blocks[::2], blocks[1::2]):
    try:
        sample = dict((m.group(1), eval(m.group(2)))
                      for m in re.finditer('(.*)\s*:\s*(.*)', values))
    except SyntaxError:
        continue

    sample['timestamp'] = datetime.strptime(timestamp, '%a %b %d %H:%M:%S %Y').timestamp()
    samples.append(sample)

print(json.dumps({
    'firmware': firmware,
    'config': config,
    'samples': samples
}))
