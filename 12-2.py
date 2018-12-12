
def simulate(ngen, init, rules):
    pots = list("..." + init + ("." * 1500))
    gens = [ init ]

    for n in range(ngen):
        npots = list(pots)
        for i in range(0, len(pots)-3):
            if i == 0:
                sub = [".", "."] + pots[:3]
            elif i == 1:
                sub = ["."] + pots[0:4]
            else:
                sub = pots[i-2:i+3]
            npots[i] = rules.get("".join(sub), ".")
        pots = npots

        spots = "".join(pots)
        gens.append(spots)
        # print("%10d:" % (n+1), "".join(pots))
    return gens


def calc(pots):
    ans = 0
    for i in range(len(pots)):
        ans += (i-3) if pots[i] == "#" else 0
    return ans


if __name__ == '__main__':
    # with open("input/12.test") as f:
    with open("input/12.txt") as f:
        lines = f.read().split("\n")

    pots = lines[0].split(":")[1].strip()
    rules = dict()
    for line in lines[2:]:
        [k, v] = line.split("=>")
        k = k.strip()
        v = v.strip()
        rules[k] = v

    gens = simulate(300, pots, rules)
    # for i in range((gens)-50, len(gens)):
    for i in range(0, len(gens)):
        print("%10d:" % i, gens[i])

    anss = [calc("".join(g)) for g in gens]
    print(anss[-20:])

    # I can see the pattern after large enough steps
    pattern = "#...#...#...#...#...#...#...#...#.####...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#..####...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#..####"
    n200 = 200
    l200 = 121
    ngen = 50000000000

    l = l200 + (ngen - n200)
    ans = 0
    for i in range(len(pattern)):
        ans += (i+l-3) if pattern[i] == "#" else 0
    print(ans)
