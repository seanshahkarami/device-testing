#!/usr/bin/env python3
import json

# ...figure out how to do bulk loading...

for device in ['dev0', 'dev1', 'dev2', 'dev3']:
    with open('{}.json'.format(device)) as f:
        data = json.load(f)

    for sample in data['samples']:
        try:
            body = {
                'device': device,
                'timestamp': int(sample['timestamp'] * 1000),
                'pm_1': sample['pm1'],
                'pm_2_5': sample['pm2.5'],
                'pm_10': sample['pm10'],
                'sample_flow_rate': sample['sample flow rate'],
            }

            try:
                body['hex'] = sample['hex']
            except KeyError:
                pass

            index = {
                'index': {
                    '_index': 'testing',
                    '_type': 'opcdata',
                }
            }

            print(json.dumps(index))
            print(json.dumps(body))
        except KeyError:
            continue
