import string
import pprint
import collections
import heapq


def topological_sort(g: dict):
    # count number of edges into each node
    ins = {u: 0 for u in g}
    for u in g:
        for v in g[u]:
            ins[v] += 1

    res = []

    # use heap as a priority queue to follow alphabetical order
    q = [u for u, n in ins.items() if n == 0]
    heapq.heapify(q)
    while q:
        u = heapq.heappop(q)
        res.append(u)

        # remove edges from u
        for v in g[u]:
            ins[v] -= 1
            if ins[v] == 0:
                heapq.heappush(q, v)
    return res


def main():
    import string
    g = {u: [] for u in string.ascii_uppercase}

    nodes = set()
    # with open("input/7.test") as f:
    with open("input/7.txt") as f:
        for line in f:
            sp = line.split()
            u, v = sp[1], sp[7]
            g[u].append(v)
            nodes.add(u)
            nodes.add(v)
    g = {u: g[u] for u in g.keys() if u in nodes}

    ans = "".join(topological_sort(g))
    print(ans)


if __name__ == '__main__':
    main()
