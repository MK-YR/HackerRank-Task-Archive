from math import gcd

gcache = {}
hcache = {}
def G(n):
    if n in gcache: return gcache[n]
    sqrtN = int(n ** .5)
    s = n * (n + 1) // 2
    for g in range(2, sqrtN + 1):
        s -= G(n // g)
        if g != n // g:
            s -= G(g) * (n // g - n // (g + 1))
    if n > 1:
        s -= G(1) * (n // 1 - n // (1 + 1))
    gcache[n] = s
    return gcache[n]
def H(n):
    if n in hcache: return hcache[n]
    s = n
    sqrtN = int(n ** .5)
    for g in range(2, sqrtN + 1):
        s += n // g - H(n // g // g)
    hcache[n] = s
    return s
def S(n):
    s = 0
    sqrtN = int(n ** .5)
    s -= G(sqrtN)
    s += H(n)
    return s - n + 1
n = int(input())
print(S(n))
