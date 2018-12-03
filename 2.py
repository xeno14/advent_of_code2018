import sys

a = [s for s in sys.stdin.readlines()]

def countnum(s, num):
    ss = set(s)
    s = "".join(sorted(s))
    for x in ss:
        l = s.find(x)
        r = s.rfind(x)
        if r-l+1 == num:
            return True
    return False

assert(countnum("abcdef", 2) == False)
assert(countnum("ababa", 2) == True)
assert(countnum("ababa", 3) == True)
assert(countnum("ababab", 3) == True)

cnt2 = sum(map(lambda x: countnum(x,2), a))
cnt3 = sum(map(lambda x: countnum(x,3), a))

print(cnt2 * cnt3)


