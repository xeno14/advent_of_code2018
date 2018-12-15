import itertools

def age(a, p1, p2):
    n = a[p1] + a[p2]

    if n >= 10:
        a.append(1)
    a.append(n%10)
    p1 = (p1 + a[p1] + 1) % len(a)
    p2 = (p2 + a[p2] + 1) % len(a)
    return (a,p1,p2)


if __name__ == '__main__':
    a = [3,7]
    p1 = 0
    p2 = 1
    # after = 2018
    after = 640441

    for i in range(after + 20):
        (a, p1, p2) = age(a, p1, p2)

    ans = a[after: after+10]
    print("".join(map(str,ans)))
