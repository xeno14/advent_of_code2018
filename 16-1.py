

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
        part1 = f.read().split("\n\n\n")[0]
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

    print(samples)
    ans = 0
    for sample in samples:
        print(sample)
        cnt = 0
        for opname in OPERATORS:
            opr = sample["operate"]
            opr[0] = opname
            result = operate(opr, sample["before"])
            if result == sample["after"]:
                cnt += 1
                print(opname, sample)

        ans += int(cnt >= 3)
    print(ans)


if __name__ == '__main__':
    main()
