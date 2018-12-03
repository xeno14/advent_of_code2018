import sys
from itertools import cycle

a = [int(s) for s in sys.stdin.readlines()]
s = 0
seen = set([s])

for x in cycle(a):
    s += x
    # print(s)
    if s in seen:
        print(s)
        break
    seen.add(s)
