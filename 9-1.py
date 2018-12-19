import itertools


def nextstep(marbles, pos, m):
    score = 0
    if m % 23 == 0:
        pos = pos - 7
        pos = pos if pos >= 0 else pos + len(marbles)
        score = marbles.pop(pos) + m
    else:
        pos = (pos + 2) % len(marbles)
        if pos == 0:
            pos = len(marbles)
        marbles.insert(pos, m)

    return marbles, pos, m + 1, score


def solve(nplayers, last_marble, verbose=False):
    marbles = [ 0, 1 ]
    pos = 1
    players = itertools.cycle(range(0, nplayers))
    _ = next(players)
    scores = [0] * nplayers

    m = 2
    while m <= last_marble:
        player = next(players)
        marbles, pos, m, score = nextstep(marbles, pos, m)

        if verbose:
            print(player+1, "\t", marbles, score)

        scores[player] += score

    return max(scores)


if __name__ == '__main__':
    assert solve(9, 25, True) == 32
    assert solve(10, 1618) == 8317
    assert solve(13, 7999) == 146373
    assert solve(21, 6111) == 54718
    assert solve(30, 5807) == 37305

    ans = solve(479, 71035)
    print(ans)

