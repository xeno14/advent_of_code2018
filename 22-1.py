import numpy as np


def get_risk(depth, tx, ty, verbose=False):
    MOD = 20183

    erosion = np.zeros((tx+1, ty+1), dtype=np.int)

    # calc geologic index
    for x in range(erosion.shape[0]):
        erosion[x, 0] = (x * 16807 + depth) % MOD
    for y in range(erosion.shape[1]):
        erosion[0, y] = (y * 48271 + depth) % MOD
    for x in range(1, erosion.shape[0]):
        for y in range(1, erosion.shape[1]):
            erosion[x, y] = (erosion[x-1,y] * erosion[x,y-1] + depth) % MOD
    erosion[0, 0] = erosion[tx, ty] = depth % MOD

    risk = erosion % 3

    if verbose:
        for y in range(risk.shape[1]):
            line = "".join(map(lambda r:"." if r==0 else "=" if r==1 else "|", risk[:,y]))
            print(line)

    return risk


def main():
    assert get_risk(510, 10, 10).sum() == 114

    risk = get_risk(11991, 6, 797)
    print(risk.sum())


if __name__ == '__main__':
    main()