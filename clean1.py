#!/usr/bin/env python3
import re
import json
import sys


device = sys.argv[1]
body = sys.stdin.read()

for values in re.split('\n\n+', body):
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
