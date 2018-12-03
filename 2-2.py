import sys

a = [s for s in sys.stdin.readlines()]

def distance(s, t):
    return len(s)-sum([x==y for x, y in zip(s,t)])

assert(distance("abc", "abc")==0)
assert(distance("abcde", "axcye")==2)
assert(distance("fghij", "fguij")==1)

for x in a:
    for y in a:
        if distance(x,y) == 1:
            print(x)

