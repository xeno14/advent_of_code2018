

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

    print(rules)
    ngen = 20
    print(pots)
    pots = list("..." + pots + "............................................")
    for n in range(ngen):
        npots = list(pots)
        for i in range(0, len(pots)-5):
            if i == 0:
                sub = [".", "."] + pots[:3]
            elif i == 1:
                sub = ["."] + pots[0:4]
            else:
                sub = pots[i-2:i+3]
            npots[i] = rules.get("".join(sub), ".")
        pots = npots
        print("%2d:" % (n+1), "".join(pots))

    ans = 0
    for i in range(len(pots)):
        ans += (i-3) if pots[i] == "#" else 0
    print(ans)


