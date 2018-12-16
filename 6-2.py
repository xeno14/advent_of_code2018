import re
import numpy as np


def dist(p, q):
    return np.abs(p[0]-q[0]) + np.abs(p[1]-q[1])


assert dist((2,3), (4,5)) == 4
assert dist((1,1), (4,1)) == 3


if __name__ == '__main__':
    with open("input/6.txt") as f:
    # with open("input/6.test") as f:
        limit = 10000

        points = []
        for l in f:
            p = re.search("(\d+), (\d+)", l).groups()
            points.append(tuple(map(int, p)))

    points = np.array(points, dtype=np.int)

    print(points)
    xmin = points[:,0].min()-1
    xmax = points[:,0].max()+1
    ymin = points[:,1].min()-1
    ymax = points[:,1].max()+1

    field = np.zeros((xmax-xmin+1, ymax-ymin+1), dtype=np.int)

    for x in range(xmin, xmax+1):
        for y in range(ymin, ymax+1):
            dists = [dist((x,y), p) for p in points]
            tot = sum(dists)
            i = x - xmin
            j = y - ymin
            field[i, j] = tot

    # print(field)

    ans = (field < limit).sum()
    print(ans)
