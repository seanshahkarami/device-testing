#!/usr/bin/env python3
import re
import json
import sys

for filename in sys.argv[1:]:
    with open(filename) as f:
        firmware = eval(f.readline()).decode()
        config = eval(f.readline())
        body = f.read()

    device = filename.split('.')[0]

    # print(json.dumps({'index': {'_index': 'alphasense-config', '_type': 'device'}}))
    # print(json.dumps({'firmware': firmware, 'config': config, 'device': device}))

    blocks = list(map(str.strip, re.split('---', body)))

    for values in blocks[1::2]:
        try:
            sample = dict((m.group(1), eval(m.group(2)))
                          for m in re.finditer('(.*)\s*:\s*(.*)', values))
        except SyntaxError:
            continue

        try:
            doc = {
                'device': device,
                'timestamp': sample['Time'] * 1000,
                'pm_1': sample['pm1'],
                'pm_2_5': sample['pm2.5'],
                'pm_10': sample['pm10'],
                'sample_flow_rate': sample['sample flow rate'],
            }

            print(json.dumps({'index': {'_index': 'testing', '_type': 'opcdata'}}))
            print(json.dumps(doc))
        except:
            continue
