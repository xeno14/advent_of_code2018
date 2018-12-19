import itertools


class Elem:

    def __init__(self, nxt, prev, val):
        self.next = nxt
        self.prev = prev
        self.val = val

    def go_next(self, n=1):
        e = self
        for i in range(n):
            e = e.next
        return e

    def go_prev(self, n=1):
        e = self
        for i in range(n):
            e = e.prev
        return e


class CircularList:

    def __init__(self, val):
        e = Elem(None, None, 0)
        e.prev = e.next = e
        self.size = 1
        self.e0 = e

    def remove(self, e):
        e.prev.next = e.next
        e.next.prev = e.prev

        self.size -= 1
        return e.next

    def get_begin(self):
        return self.e0

    def insert(self, e, val):
        ee = Elem(e.next, e, val)
        e.next.prev = ee
        e.next = ee
        self.size += 1
        return ee

    def show_all(self):
        e = self.e0
        for i in range(self.size):
            print(e.val, end=" ")
            e = e.next
        print()


def nextstep(marbles: CircularList, e: Elem, m: int):
    score = 0
    if m % 23 == 0:
        e = e.go_prev(7)
        score = e.val + m
        e = marbles.remove(e)
    else:
        e = e.go_next(1)
        e = marbles.insert(e, m)  # insert *after*

    return marbles, e, m + 1, score


def solve(nplayers, last_marble, verbose=False):
    marbles = CircularList(0)
    e = marbles.get_begin()
    e = marbles.insert(e, 1)

    players = itertools.cycle(range(0, nplayers))
    _ = next(players)
    scores = [0] * nplayers

    m = 2
    while m <= last_marble:
        print("{}/{} - {:.1%}%".format(m, last_marble, m/last_marble))
        player = next(players)
        marbles, e, m, score = nextstep(marbles, e, m)

        if verbose:
            marbles.show_all()

        scores[player] += score

    return max(scores)


def main():
    assert solve(9, 25, True) == 32
    assert solve(10, 1618) == 8317
    assert solve(13, 7999) == 146373
    assert solve(21, 6111) == 54718
    assert solve(30, 5807) == 37305

    print(solve(479, 71035 * 100))


if __name__ == '__main__':
    main()

