from __future__ import division, print_function
import csv
from pprint import pprint

data = []
# read file with delimiter line by line
with open('dataset/record_10000_D.txt') as f:
    c = csv.reader(f, delimiter='\t', skipinitialspace=True)
    print('reading')
    for line in c:
        data.append(line)

#data = [(arr[:3] + arr[4:]) for arr in data]

dlen = len(data)
x, y, t = -1, -1, -1
pprint(data)

for r in range(dlen):
    print('pre-processing %d / %d' % (r + 1, dlen))
    data[r][1] = str(int(float(data[r][1]) * 199.9928479379))
    data[r][2] = str(int(float(data[r][2]) * 199.9924833285))
    data[r][3] = data[r][3].split(':')[0]

r = 0
dlen = len(data)
for r in range(len(data) - 1, -1, -1):
    print('delete duplications %d / %d' % (r, dlen))
    _x = data[r][1]
    _y = data[r][2]
    _t = data[r][3]
    if (int(_t) > 9 and int(_t) < 21) and (x != _x or y != _y) and t != _t:
        x = _x
        y = _y
        t = _t
    else:
        del data[r]

with open('dataset/record_10000_D_grid.txt', 'w') as f:
    for l, el in enumerate(data):
        string = ' '.join(map(str, el))
        for item in string:
            print()
            f.write(item)
        f.write('\n')

dirs = {8: 'NW', 12: 'NE', -12: 'SW', -8: 'SE', 10: 'N', -10: 'S', 2: 'E', -2: 'W'}


class PT:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    x = int()
    y = int()


dlen = len(data)
path = []
_id = '-1'
prev_data = []
for i in range(len(data)):
    print('mapping paths %d / %d' % (i + 1, dlen))
    if data[i][0] != _id:
        cp = PT(data[i][1], data[i][2])
        if len(prev_data) > 0:
            path.append(prev_data)
        prev_data = []
        _id = data[i][0]
        continue
    np = PT(data[i][1], data[i][2])
    ns_df = np.y - cp.y
    ns_df /= abs(ns_df) if ns_df != 0 else 1
    ew_df = np.x - cp.x
    ew_df /= abs(ew_df) if ew_df != 0 else 1
    ew_df *= 2
    cp = np
    prev_data.append('%s %s' % (dirs[int(ns_df * 10 + ew_df)], data[i][3]))
    print(prev_data)
if len(prev_data) > 0:
    path.append(prev_data)

with open('dataset/record_10000_D_path.txt', 'w') as f:
    for l, el in enumerate(path):
        string = ' '.join(map(str, el))
        for item in string:
            f.write(item)
        f.write('\n')
