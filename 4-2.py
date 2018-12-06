import sys
import re
import datetime

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
            guard_mins[guard] = guard_mins.get(guard, []) + [(start, end)]

    cnt_ans = 0
    for g, rng in guard_mins.items():
        for i in range(0, 60):
            cnt = sum([r[0] <= i <= r[1] for r in rng])
            if cnt_ans < cnt:
                cnt_ans = cnt
                g_ans = g
                m_ans = i
    print(g_ans, m_ans, cnt_ans, g_ans*m_ans)



