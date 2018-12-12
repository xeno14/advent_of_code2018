def parse(data):
    nchild = data[0]
    nmeta = data[1]
    l = 2
    child = []
    for i in range(nchild):
        ll, c = parse(data[l:])
        child.append(c)
        l += ll
    meta = data[l:l+nmeta]
    l += nmeta
    node = dict(meta=meta, child=child)
    return l, node


def calc(tree):
    child = tree["child"]
    meta = tree["meta"]

    # cache
    if "value" in tree:
        return tree["value"]

    if len(child) == 0:
        tree["value"] = sum(meta)
    else:
        res = 0
        for i in meta:
            idx = i - 1
            if idx < len(child):
                res += calc(child[idx])
        tree["value"] = res
    return tree["value"]


if __name__ == '__main__':
    with open("input/8.txt") as f:
    # with open("input/8.test") as f:
        data = [int(x) for x in f.read().split()]
    print(data)

    _, tree = parse(data)
    print(calc(tree))


