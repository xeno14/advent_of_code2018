def parse_time(line):
    # return datetime.datetime.strptime(line[1:17], "%Y-%m-%d %H:%M")
    return int(line.split(" ")[1][3:5])


assert(parse_time("[1518-11-01 00:05] falls asleep") == 5)


if __name__ == '__main__':
    # sort logs
    #with open("input/4-1.test") as f:
    with open("input/4.txt") as f:
        a = f.read().split("\n")

    a = sorted(a, key=lambda x: x.split("]")[0])
    # with open("4_sorted.txt", "w") as f:
    #     f.write("\n".join(a))

    guards = dict()
    guard_mins = dict()

    for line in a:
        if "Guard" in line:
            l = line.find("#") + 1
            r = line.find("begins") - 1
            guard = int(line[l:r])
        if "falls asleep" in line:
            start = parse_time(line)
        if "wakes up" in line:
            end = parse_time(line)
            guards[guard] = guards.get(guard, []) + [end-start]
            guard_mins[guard] = guard_mins.get(guard, []) + list(range(start, end))

    sleeping = sorted([(k, v) for k,v in guards.items()], key=lambda x: sum(x[1]), reverse=True)
    g = sleeping[0][0]

    mins = guard_mins[g]
    import collections
    c = collections.Counter(mins).most_common()
    m = c[0][0]

    print(g, m, g*m)
