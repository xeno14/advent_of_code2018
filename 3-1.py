import numpy as np
import re


if __name__ == '__main__':
    with open("input/3.txt") as f:
    # with open("input/3.test") as f:
        claims = []
        for l in f:
            c = re.search(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", l).groups()
            claims.append(tuple(map(int, c)))

    print(claims)

    grid = np.zeros((1000, 1000), dtype=np.int)

    for claim in claims:
        _, x, y, w, h = claim
        grid[x:x+w, y:y+h] += 1

    ans = np.sum(grid>=2)

    print(grid[:10,:10])

    print(ans)