from math import sqrt

for _ in range(int(input())):
    d, p = map(int, input().split())
    if d < 0:
        print(0)
        continue
    nb = 0
    D = d * d + 4 * p
    if D < 0:
        print(0)
        continue
    b = int((-d - sqrt(D)) / 2)
    a = d + b
    if a * b == p:
        nb += 1
        if a != b:
            nb += 1
    if D != 0:
        b = int((-d + sqrt(D)) / 2)
        a = d + b
        if a * b == p:
            nb += 1
            if a != b:
                nb += 1
    print(nb)