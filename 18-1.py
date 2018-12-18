import numpy as np


VOID = 0
OPEN = 1
TREE = 2
LUMBERYARD = 3


def next_grid(a, nsize):
    res = a.copy()

    for i in range(1, nsize+1):
        for j in range(1, nsize+1):
            # print(i,j)
            rel_pos = np.array([
                [-1,-1], [0,-1], [1,-1],
                [-1, 0],         [1, 0],
                [-1, 1], [0, 1], [1, 1],
            ])

            adjacent = np.array([a[i+dx,j+dy] for dx, dy in rel_pos])
            # print(i, j, adjacent)

            cell = a[i,j]
            if cell == OPEN and np.sum(adjacent == TREE) >= 3:
                res[i,j] = TREE
            elif cell == TREE and np.sum(adjacent == LUMBERYARD) >= 3:
                res[i,j] = LUMBERYARD
            elif cell == LUMBERYARD:
                n1 = np.sum(adjacent == TREE)
                n2 = np.sum(adjacent == LUMBERYARD)
                # if i == 9 and j == 1:
                #     print("hi")
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

    for i in range(10):
        grid = next_grid(grid, nsize)
        visualize(grid.T)
        print()

    ntree = np.sum(grid == TREE)
    nlumb = np.sum(grid == LUMBERYARD)
    print("{} * {} = {}".format(ntree, nlumb, ntree*nlumb))


if __name__ == '__main__':
    main()