import string
import pprint

if __name__ == '__main__':
    m = dict()

    froms = []
    tos = []
    # with open("input/7.test") as f:
    with open("input/7.txt") as f:
        nworker = 5
        cost_offset = 60
        for line in f:
            sp = line.split()
            froms.append(sp[1])
            tos.append(sp[7])
    keys = set(froms + tos)
    m = {k:set() for k in keys}
    for frm, to in zip(froms, tos):
        m[to].add(frm)

    import string
    cost_map = {k:(v + cost_offset) for k, v in zip(string.ascii_uppercase, range(1,27))}
    print(cost_map)

    ans = ""
    workers = [{"job":"", "t": 0} for i in range(nworker)]

    print(m, nworker)

    tick = 0
    while True:
        tick += 1
        print(workers, m)
        for i in range(len(workers)):
            if workers[i]["job"] == "":
                continue

            workers[i]["t"] -= 1

            # completed a task
            if workers[i]["t"] <= 0 and workers[i]["job"] != "":
                r = workers[i]["job"]
                workers[i]["job"] = ""
                for k in m:
                    if r in m[k]:
                        m[k].remove(r)

        ready = sorted([k for k, v in m.items() if len(v) == 0])

        for r in ready:
            for i in range(len(workers)):
                # assign a task if a worker is free
                if workers[i]["t"] <= 0:
                    workers[i] = {
                        "t": cost_map[r],
                        "job": r,
                    }
                    ans += r

                    print("assigned {} to {}".format(r, i))
                    del m[r]
                    break

        if len(m) == 0 and sum([w["t"] for w in workers]) == 0:
            break
    print(tick-1, ans)





