import pprint


def geti(r, i):
    return r[i]

def getr(opr, r, i):
    ii = opr[i]
    return r[ii]


OPERATORS = [
     "addr",
     "addi",
     "mulr",
     "muli",
     "banr",
     "bani",
     "borr",
     "bori",
     "setr",
     "seti",
     "gtir",
     "gtri",
     "gtrr",
     "eqir",
     "eqri",
     "eqrr",
]

def operate(opr, r):
    # print(opr, r)
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
    assert operate(["mulr", 2, 1, 2], [3, 2, 1, 1]) == [3,2,2,1]
    assert operate(["addi", 2, 1, 2], [3, 2, 1, 1]) == [3,2,2,1]
    assert operate(["seti", 2, 1, 2], [3, 2, 1, 1]) == [3,2,2,1]
    assert len(set(OPERATORS)) == len(OPERATORS)
    assert len(OPERATORS) == 16

    samples = []
    # with open("input/16.test") as f:
    with open("input/16.txt") as f:
        part1, part2 = f.read().split("\n\n\n")
        part2 = part2.strip()
        for s in part1.split("\n\n"):
            lines = s.split("\n")
            before = map(int, lines[0].split("[")[1][:-1].split(","))
            op = map(int, lines[1].split())
            after = map(int, lines[2].split("[")[1][:-1].split(","))
            samples.append({
                "before": list(before),
                "operate": list(op),
                "after": list(after)
            })

    opmap = {
        k: set(OPERATORS) for k in range(len(OPERATORS))
    }

    for sample in samples:
        for opname in OPERATORS:
            opr = list(sample["operate"])
            opr[0] = opname
            result = operate(opr, sample["before"])

            if result != sample["after"]:
                opn = sample["operate"][0]
                if opname in opmap[opn]:
                    opmap[opn].remove(opname)
                    print("remove {} from {}".format(opname, opn))
    pprint.pprint(opmap)

    # find op digit to op name mapping
    final_opmap = dict()
    while True:
        is_updated = False
        for k, v in opmap.items():
            if len(v) == 1 and k not in final_opmap:
                final_opmap[k] = list(v)[0]
        # remove from other keys
        for kk in opmap:
            for opname in [v for v in final_opmap.values()]:
                if opname in opmap[kk]:
                    opmap[kk].remove(opname)
        if len(final_opmap) == len(OPERATORS):
            break

    pprint.pprint(final_opmap)

    r = [0,0,0,0]
    programs = [list(map(int,l.split())) for l in part2.split("\n")]
    print(programs)
    for opr in programs:
        opr[0] = final_opmap[opr[0]]
        r = operate(opr, r)

    print(r)


if __name__ == '__main__':
    main()
