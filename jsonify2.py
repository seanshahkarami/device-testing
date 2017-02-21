#!/usr/bin/env python3
from alphasense.opc import decode18
import json
import sys
from binascii import hexlify
import re

samples = []

for n, line in enumerate(open(sys.argv[1])):

    match = re.match('(\d+)\s*Bins:\s*(.*)', line)

    if match is None:
        continue

    timestamp = int(match.group(1))
    data = bytes([int(x, 16) for x in match.group(2).split()])

    if len(data) != 62:
        continue

    sample = decode18(data)
    sample['timestamp'] = timestamp
    sample['hex'] = ' '.join(re.findall('\w{2}', hexlify(data).decode()))
    samples.append(sample)

data = {
    'firmware': 'unknown',
    'config': 'unknown',
    'samples': samples
}

print(json.dumps(data))
