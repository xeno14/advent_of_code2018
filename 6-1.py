import re
import numpy as np


def dist(p, q):
    return np.abs(p[0]-q[0]) + np.abs(p[1]-q[1])


assert dist((2,3), (4,5)) == 4
assert dist((1,1), (4,1)) == 3


if __name__ == '__main__':
    with open("input/6.txt") as f:
        # with open("input/6.test") as f:
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
            #print((x,y), sorted(dists))

            pp = np.argmin(dists)
            # print(x, y, dists, pp)

            d = dists[pp]

            # possibly multiple points are closest
            if (dists==d).sum() > 1:
                pp = -1
            i = x - xmin
            j = y - ymin
            field[i, j] = pp

    candidates = set(range(len(points)))

    # remove id on edges
    for s in set(field[0,:]):
        if s in candidates:
            candidates.remove(s)
    for s in set(field[-1,:]):
        if s in candidates:
            candidates.remove(s)
    for s in set(field[:,0]):
        if s in candidates:
            candidates.remove(s)
    for s in set(field[:,-1]):
        if s in candidates:
            candidates.remove(s)
    print(candidates)

    areas = [ (field==c).sum() for c in candidates]
    ans = max(areas)
    print(ans)
