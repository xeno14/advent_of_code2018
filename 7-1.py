import string
import pprint

if __name__ == '__main__':
    m = dict()

    froms = []
    tos = []
    #with open("7.test") as f:
    with open("input/7.txt") as f:
        for line in f:
            sp = line.split()
            froms.append(sp[1])
            tos.append(sp[7])
    keys = set(froms + tos)
    m = {k:set() for k in keys}
    for frm, to in zip(froms, tos):
        m[to].add(frm)

    ans = ""
    print(m)
    while len(m) > 0:
        ready = sorted([k for k, v in m.items() if len(v) == 0])
        print(ready)

        r = ready[0]
        ans += r
        del m[r]
        for k in m:
            if r in m[k]:
                m[k].remove(r)
    print(ans)





