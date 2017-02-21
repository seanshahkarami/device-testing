import numpy as np
import numpy.linalg as la
import json

with open('dev0.json') as f:
    data = json.load(f)

A = []
b = []

for sample in data['samples']:
    try:
        r = sample['bins']
        p = sample['pm1']
        A.append(r)
        b.append(p)
    except KeyError:
        continue

A = np.asarray(A)
b = np.asarray(b)
x, residuals, rank, _ = la.lstsq(A, b)

print(x)
print(residuals[0])
