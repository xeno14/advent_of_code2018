import numpy as np
import re


def dist(x1, x2):
    return np.absolute(x1-x2).sum()


def solve(filename):
    with open(filename) as f:
        # with open("input/23.txt") as f:
        points = []

        for line in f.readlines():
            (x,y,z,w) = map(int, re.search(r"(.+),(.+),(.+),(.+)", line).groups())

            points.append([x,y,z,w])
    points = np.array(points)
    # print(points)

    adj = dict()  # adjacent list

    for i in range(len(points)):
        adj[i] = list()
        for j in range(len(points)):
            if i == j:
                continue
            if dist(points[i], points[j])  <= 3:
                adj[i].append(j)

    cols = dict()  # index -> constellation
    col = 0

    for idx in range(len(points)):
        if idx in cols:
            continue

        stack = list()
        stack.append(idx)
        cols[idx] = col

        # search all adjacent stars
        while len(stack) > 0:
            i = stack.pop()
            for j in adj[i]:
                if j in cols:
                    continue
                cols[j] = col
                stack.append(j)
        col += 1
    return col


def main():
    assert solve("input/25_1.test") == 2
    assert solve("input/25_2.test") == 4
    assert solve("input/25_3.test") == 3
    assert solve("input/25_4.test") == 8

    ans = solve("input/25.txt")
    print(ans)


if __name__ == '__main__':
    main()
