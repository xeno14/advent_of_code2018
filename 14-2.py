import itertools

def age(a, p1, p2):
    n = a[p1] + a[p2]

    if n >= 10:
        a.append(1)
    a.append(n%10)
    p1 = (p1 + a[p1] + 1) % len(a)
    p2 = (p2 + a[p2] + 1) % len(a)
    return (a,p1,p2)


def find(a, p1, p2, target):
    rpt = 0
    while True:
        print(rpt)
        rpt += 1

        (a, p1, p2) = age(a, p1, p2)

        s = "".join(map(str, a[-len(target)*2:]))

        i = s.find(target)
        if i >= 0:
            res = len(a) - len(target) * 2 + i
            break
    return res


if __name__ == '__main__':
    assert find([3,7],0,1,"51589") == 9
    assert find([3,7],0,1,"01245") == 5
    assert find([3,7],0,1,"92510") == 18
    assert find([3,7],0,1,"59414") == 2018

    ans = find([3,7], 0, 1,"640441")
    print(ans)
