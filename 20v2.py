import numpy as np


class DistanceMap:
    """map x,y -> distance
    """
    INF = (1 << 20)

    def __init__(self):
        self.map = dict()
        self.set(0, 0, 0)

    def set(self, x, y, d):
        pos = (x, y)
        if pos not in self.map:
            self.map[pos] = DistanceMap.INF
        self.map[pos] = min(self.get(x, y), d)

    def get(self, x, y):
        return self.map[(x, y)]

    def as_array(self):
        pos = np.array([[x, y] for x, y in self.map.keys()])
        xmin = pos[:,0].min()
        xmax = pos[:,0].max()
        ymin = pos[:,1].min()
        ymax = pos[:,1].max()

        nx = xmax - xmin + 1
        ny = ymax - ymin + 1

        res = np.zeros((nx, ny), dtype=np.int)
        for x, y in pos:
            i = x - xmin
            j = y - ymin
            res[i, j] = self.get(x, y)
        return res

    def print(self):
        grid = self.as_array()
        grid[grid == self.INF] = -1
        print(grid.T[::-1])


def parse(regex: str) -> DistanceMap:
    if regex.startswith("^"):
        regex = regex[1:]
    if regex.endswith("$"):
        regex = regex[:-1]

    DELTA_POS = dict(N=(0, 1), E=(1, 0), W=(-1, 0), S=(0, -1))

    stack = []
    pos = [0, 0]
    dist = DistanceMap()
    dist.set(0, 0, 0)
    for c in regex:
        if c == "(":
            stack.append(pos)
        elif c == ")":
            pos = stack.pop()
        elif c == "|":
            pos = stack[-1]
        else:
            delta = DELTA_POS[c]
            npos = (pos[0] + delta[0], pos[1] + delta[1])
            dist.set(*npos, dist.get(*pos) + 1)
            pos = npos
    return dist


def solve(regex: str) -> int:
    return parse(regex).as_array().max()


def solve2(regex: str) -> int:
    return sum(parse(regex).as_array().flatten() >= 1000)


def main():
    assert solve("^WNE$") == 3
    assert solve("^ENWWW(NEEE|SSE(EE|N))$") == 10
    assert solve("^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$") == 18
    assert solve("^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$") == 23
    assert solve("^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$") == 31

    with open("input/20.txt") as f:
        regex = f.read().strip()

    print("part1 =", solve(regex))
    print("part2 =", solve2(regex))


if __name__ == '__main__':
    main()