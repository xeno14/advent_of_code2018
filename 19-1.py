
# copied from day16

def geti(r, i):
    return r[i]


def getr(opr, r, i):
    ii = opr[i]
    return r[ii]


def operate(opr, r):
    r = list(r)  # copy
    opname = opr[0]
    if opname == "addr":
        r[opr[3]] = getr(opr, r, 1) + getr(opr, r, 2)
    elif opname == "addi":
        r[opr[3]] = getr(opr, r, 1) + geti(opr, 2)
    elif opname == "mulr":
        r[opr[3]] = getr(opr, r, 1) * getr(opr, r, 2)
    elif opname == "muli":
        r[opr[3]] = getr(opr, r, 1) * geti(opr, 2)
    elif opname == "banr":
        r[opr[3]] = getr(opr, r, 1) & getr(opr, r, 2)
    elif opname == "bani":
        r[opr[3]] = getr(opr, r, 1) & geti(opr, 2)
    elif opname == "borr":
        r[opr[3]] = getr(opr, r, 1) | getr(opr, r, 2)
    elif opname == "bori":
        r[opr[3]] = getr(opr, r, 1) | geti(opr, 2)
    elif opname == "setr":
        r[opr[3]] = getr(opr, r, 1)
    elif opname == "seti":
        r[opr[3]] = geti(opr, 1)
    elif opname == "gtir":
        r[opr[3]] = int(geti(opr, 1) > getr(opr, r, 2))
    elif opname == "gtri":
        r[opr[3]] = int(getr(opr, r, 1) > geti(opr, 2))
    elif opname == "gtrr":
        r[opr[3]] = int(getr(opr, r, 1) > getr(opr, r, 2))
    elif opname == "eqir":
        r[opr[3]] = int(geti(opr, 1) == getr(opr, r, 2))
    elif opname == "eqri":
        r[opr[3]] = int(getr(opr, r, 1) == geti(opr, 2))
    elif opname == "eqrr":
        r[opr[3]] = int(getr(opr, r, 1) == getr(opr, r, 2))

    return r


def main():
    # with open("input/19.test") as f:
    with open("input/19.txt") as f:
        lines = list(f.readlines())
        ip_reg = int(lines[0].split()[1])
        insts = [
            [l[0]] + list(map(int, l[1:])) for l in map(lambda ll: ll.split(), lines[1:])
        ]

    r = [0] * 6

    ip = 0
    while 0 <= ip < len(insts):
        r[ip_reg] = ip
        inst = insts[ip]
        print(ip, r, inst, end=" ")
        r = operate(inst, r)
        print(r)

        ip = r[ip_reg] + 1
    print("end")
    print(r)
    print(r[0])


if __name__ == '__main__':
    main()
