import numpy as np

def calc(x, y, serial=8199):
    r = x + 10
    z = r * y
    z = z + serial
    z = z * r
    z = int(("%03d" % z)[-3])
    return z - 5

assert calc(3, 5, serial=8) == 4
assert calc(122, 79, serial=57) == -5
assert calc(217, 196, serial=39) == 0
assert calc(101, 153, serial=71) == 4
# assert calc(2, 1, serial=18) == -4

def search(grid, w):
    print(w)
    n = grid.shape[0]
    power = np.zeros((n, n), dtype=np.int)
    for i in range(0, n-w):
        for j in range(0, n-w):
            power[i,j] = grid[i:i+w,j:j+w].sum()
    return power


if __name__ == '__main__':
    import sys
    serial = int(sys.argv[1])
    # serial = 18
    # serial = 42
    # serial = 8199
    print("serial =", serial)

    grid = np.zeros((300, 300), dtype=np.int)
    for i in range(300):
        for j in range(300):
            x = i+1
            y = j+1
            grid[i, j] = calc(x, y, serial=serial)
    # print(grid[31:36,43:48].T)

    powers = np.array([search(grid, w) for w in range(0, 300)])

    # for w in range(1, n):
    #     print(w)
    #     for i in range(0, n-w):
    #         for j in range(0, n-w):
    #             power[w,i,j] = grid[i:i+w,j:j+w].sum()

    idx = np.unravel_index(np.argmax(powers), powers.shape)
    print(idx)
    print("%d,%d,%d" % (idx[1]+1, idx[2]+1, idx[0]))
