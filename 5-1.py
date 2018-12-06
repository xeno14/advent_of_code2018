with open("input/5.txt") as f:
#with open("input/5.test") as f:
    poly = f.read().strip()

def is_reactable(x,y):
    return x.lower()==y.lower() and x.islower() != y.islower()

assert(not is_reactable("a", "a"))
assert(not is_reactable("a", "B"))
assert(is_reactable("a", "A"))

print(len(poly))

result = ""
for p in poly:
    if len(result)==0:
        result += p
        continue

    q = result[-1]  # tail
    if is_reactable(p, q):
        result = result[:-1]  # remove tail
    else:
        result += p

print(len(result))

