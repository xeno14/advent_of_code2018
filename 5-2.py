with open("input/5.txt") as f:
#with open("input/5.test") as f:
    poly = f.read().strip()

def is_reactable(x,y):
    return x.lower()==y.lower() and x.islower() != y.islower()

def react(poly: str):
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
    return result

import string
lens = []
for c in string.ascii_lowercase:
    new_poly = poly.replace(c, "").replace(c.upper(), "")
    l = len(react(new_poly))
    lens.append(l)

print(min(lens))



