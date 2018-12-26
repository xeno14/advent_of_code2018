import numpy as np
from enum import Enum


class Tools(Enum):
    CLIMB = 0
    TORCH = 1
    NEITHER = 2


class Cave(Enum):
    ROCK = 0
    WET = 1
    NARROW = 2


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


def solve(depth, tx, ty, margin):
    """solver

    Risk:
        rocky    -> 0
        wet      -> 1
        narrow   -> 2

    Equipment:
        neither  -> 0
        torch    -> 1
        climbing -> 2

    risk cannot be same as equipment as shown the above.
    """

    INF = 1 << 20

    nx = tx + margin
    ny = ty + margin

    risk = get_risk(depth, nx, ny)
    risk[0, 0] = risk[tx, ty] = 0  # always rocky

    # distance[e,x,y] -> the fewest way to reach x, y with equipment e
    distance = np.zeros((3, *risk.shape), dtype=np.int)
    distance[:] = INF

    distance[1, 0, 0] = 0  # start with torch

    t = 1
    while True:
        print(t)
        t += 1
        converged = True

        for x in range(risk.shape[0] - 1):
            for y in range(risk.shape[1] - 1):
                here = risk[x, y]

                # loop for equipments
                for e in range(3):
                    if e == here:  # risk and equipment cannot be same
                        distance[e, x, y] = INF
                        continue

                    # do not change equipment
                    candidates = [
                        distance[e, x, y],
                        distance[e, x-1, y] + 1 if x > 0 else INF,
                        distance[e, x, y-1] + 1 if y > 0 else INF,
                        distance[e, x+1, y] + 1,
                        distance[e, x, y+1] + 1,
                        ]

                    # change equipment
                    e1 = (e+1) % 3
                    e2 = (e+2) % 3

                    if e1 != here:
                        candidates = candidates + [
                            distance[e1, x-1, y] + 7 + 1 if x > 0 else INF,
                            distance[e1, x, y-1] + 7 + 1 if y > 0 else INF,
                            distance[e1, x+1, y] + 7 + 1,
                            distance[e1, x, y+1] + 7 + 1,
                            ]
                    if e2 != here:
                        candidates = candidates + [
                            distance[e2, x-1, y] + 7 + 1 if x > 0 else INF,
                            distance[e2, x, y-1] + 7 + 1 if y > 0 else INF,
                            distance[e2, x+1, y] + 7 + 1,
                            distance[e2, x, y+1] + 7 + 1,
                            ]
                    d = min(candidates)

                    if d != distance[e,x,y]:
                        converged = False
                    distance[e, x, y] = d
        # continue until converged
        if converged:
            break
    return distance[1, tx, ty]  # equips torch


def main():
    # test part1
    assert get_risk(510, 10, 10).sum() == 114
    assert get_risk(11991, 6, 797).sum() == 5622

    # test part2
    assert solve(510, 10, 10, margin=10) == 45

    result = solve(11991, 6, 797, margin=200)
    print(result)


if __name__ == '__main__':
    main()