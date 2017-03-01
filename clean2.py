#!/usr/bin/env python3
from alphasense.opc import decode18
import json
from binascii import hexlify
import re
import sys


device = sys.argv[1]

for n, line in enumerate(sys.stdin):
    match = re.match('(\d+)\s*Bins:\s*(.*)', line)

    if match is None:
        continue

    timestamp = int(match.group(1))
    data = bytes([int(x, 16) for x in match.group(2).split()])

    if len(data) != 62:
        continue

    try:
        sample = decode18(data)
    except AssertionError as e:
        print('decode error: {}'.format(data), file=sys.stderr)
        continue

    hexdump = ' '.join(re.findall('\w{2}', hexlify(data).decode()))

    doc = {
        'device': device,
        'timestamp': int(timestamp * 1000),
        'pm_1': sample['pm1'],
        'pm_2_5': sample['pm2.5'],
        'pm_10': sample['pm10'],
        'sample_flow_rate': sample['sample flow rate'],
        'hex': hexdump,
    }

    print(json.dumps({'index': {'_index': 'testing', '_type': 'opcdata'}}))
    print(json.dumps(doc))
