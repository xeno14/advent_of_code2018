import numpy as np


VOID = 0
OPEN = 1
TREE = 2
LUMBERYARD = 3


# could be faster using numba.stencil
def next_grid(a, nsize):
    res = a.copy()

    for i in range(1, nsize+1):
        for j in range(1, nsize+1):
            rel_pos = np.array([
                [-1,-1], [0,-1], [1,-1],
                [-1, 0],         [1, 0],
                [-1, 1], [0, 1], [1, 1],
            ])

            adjacent = np.array([a[i+dx,j+dy] for dx, dy in rel_pos])

            cell = a[i,j]
            if cell == OPEN and np.sum(adjacent == TREE) >= 3:
                res[i,j] = TREE
            elif cell == TREE and np.sum(adjacent == LUMBERYARD) >= 3:
                res[i,j] = LUMBERYARD
            elif cell == LUMBERYARD:
                n1 = np.sum(adjacent == TREE)
                n2 = np.sum(adjacent == LUMBERYARD)
                if n1 >= 1 and n2 >= 1:
                    res[i,j] = LUMBERYARD
                else:
                    res[i,j] = OPEN
    return res


def visualize(a):
    for row in a:
        line = ""
        for cell in row:
            if cell == OPEN:
                line += "."
            elif cell == TREE:
                line += "|"
            elif cell == LUMBERYARD:
                line += "#"
            else:
                line += ""
        print(line)


def calc(grid):
    ntree = np.sum(grid == TREE)
    nlumb = np.sum(grid == LUMBERYARD)
    return ntree * nlumb


def main():
    grid = np.zeros((101,101), dtype=np.int)  # large enough

    with open("input/18.txt") as f:
    # with open("input/18.test") as f:
        for j, line in enumerate(f.readlines()):
            nsize = len(line)
            for i in range(len(line)):
                grid[i+1,j+1] = {
                    ".": OPEN,
                    "|": TREE,
                    "#": LUMBERYARD,
                }.get(line[i], 0)

    grid = grid[0:nsize+2, 0:nsize+2]

    results = [calc(grid)]
    for i in range(1000):
        grid = next_grid(grid, nsize)
        # visualize(grid.T)
        r = calc(grid)
        print("%5d: %d" % (i+1, r))
        results.append(r)

    results = np.array(results)
    np.savetxt("18-2.txt", results)

    # continue to 18-2.ipynb


if __name__ == '__main__':
    main()