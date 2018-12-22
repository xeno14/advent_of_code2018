class Node:

    def __init__(self, val=""):
        self.parent = None
        self.children = []
        self.val = val
        self.next = None

    def append(self, e):
        e.parent = self
        self.children.append(e)

    def print(self, level=0):
        print("{}{}".format(" "*(2*level), self.val))
        for c in self.children:
            c.print(level + 1)

        if self.next is not None:
            self.next.print(level)

    def cleanup(self):
        """Remove empty nodes
        """
        children = [c for c in self.children if c.val != ""]
        self.children = children
        for c in self.children:
            c.cleanup()
        return self


def parse(s: str) -> Node:
    root = Node()
    node = Node()
    root.append(node)
    for i in range(len(s)):
        c = s[i]
        if c == "(":
            child = Node()
            node.append(child)
            node = child
        elif c == ")":
            nxt = Node()
            node = node.parent
            nxt.parent = node.parent
            node.next = nxt
            node = nxt
        elif c == "|":
            child = Node()
            node.parent.append(child)
            node = child
        else:
            node.val += c
    return root.cleanup()


class DistanceMap:
    """map x,y -> distance
    """
    INF = (1 << 20)

    def __init__(self):
        self.map = dict()
        self.set(0, 0, 0)

    def set(self, x, y, d):
        if x not in self.map:
            self.map[x] = dict()
        if y not in self.map[x]:
            self.map[x][y] = DistanceMap.INF
        self.map[x][y] = min(self.map[x][y], d)

    def get(self, x, y):
        if x not in self.map:
            return DistanceMap.INF
        if y not in self.map[x]:
            return DistanceMap.INF
        return self.map[x][y]

    def find_max(self):
        res = -1
        for v in self.map.values():
            res = max(res, max(v.values()))
        return res

    def as_grid(self):
        xs = list(self.map.keys())
        ys = [y for x in xs for y in self.map[x]]
        xmin = min(xs)
        xmax = max(xs)
        ymin = min(ys)
        ymax = max(ys)

        nx = xmax - xmin + 1
        ny = ymax - ymin + 1
        import numpy as np
        grid = np.zeros((nx, ny), dtype=np.int)
        for x in xs:
            for y in ys:
                i = x - xmin
                j = y - ymin
                grid[i, j] = self.get(x, y)
        return grid

    def print(self):
        grid = self.as_grid()
        grid[grid == self.INF] = -1
        print(grid.T[::-1])


DELTA_POS = dict(N=(0, 1), E=(1, 0), W=(-1, 0), S=(0, -1))


def build_maze(root: Node, pos: tuple, dist: DistanceMap):
    node = root
    for c in node.val:
        delta = DELTA_POS[c]
        x = pos[0]
        y = pos[1]
        nx = x + delta[0]
        ny = y + delta[1]
        d = dist.get(x, y)
        dist.set(nx, ny, d+1)
        pos = (nx, ny)

    for child in node.children:
        build_maze(child, pos, dist)

    if node.next is not None:
        build_maze(node.next, pos, dist)


def solve(regex: str, verbose=False):
    """solve part1
    """
    if regex.startswith("^"):
        regex = regex[1:]
    if regex.endswith("$"):
        regex = regex[:-1]

    root = parse(regex)
    dist = DistanceMap()
    pos = (0,0)
    build_maze(root, pos, dist)
    if verbose:
        print(regex)
        root.print()
        dist.print()

    return dist.as_grid().max()


def solve2(regex: str):
    """solve part2
    """
    if regex.startswith("^"):
        regex = regex[1:]
    if regex.endswith("$"):
        regex = regex[:-1]

    root = parse(regex)
    dist = DistanceMap()
    pos = (0,0)
    build_maze(root, pos, dist)
    grid = dist.as_grid()

    return sum(grid.flatten() >= 1000)


def main():
    assert solve("^WNE$", True) == 3
    assert solve("^ENWWW(NEEE|SSE(EE|N))$", True) == 10
    assert solve("^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$", True) == 18
    assert solve("^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$", True) == 23
    assert solve("^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$", True) == 31

    with open("input/20.txt") as f:
        regex = f.read().strip()
    ans1 = solve(regex, verbose=False)
    ans2 = solve2(regex)

    print("part1 =", ans1)
    print("part2 =", ans2)


if __name__ == '__main__':
    main()