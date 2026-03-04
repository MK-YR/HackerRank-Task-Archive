#!/bin/python3

import sys

def precompute(p):
    fact = [1] * p
    invfact = [1] * p
    for i in range(1, p):
        fact[i] = fact[i-1] * i % p
    invfact[p-1] = pow(fact[p-1], p-2, p)
    for i in reversed(range(p-1)):
        invfact[i] = invfact[i+1] * (i+1) % p
    return fact, invfact
def nCr_small(n, r, p, fact, invfact):
    if r > n:
        return 0
    return fact[n] * invfact[r] % p * invfact[n-r] % p
def lucas(n, r, p, fact, invfact):
    result = 1
    while n > 0 or r > 0:
        ni = n % p
        ri = r % p
        if ri > ni:
            return 0
        result = result * nCr_small(ni, ri, p, fact, invfact) % p
        n //= p
        r //= p
    return result
def solve(N, K, p):
    fact, invfact = precompute(p)
    return lucas(N+1, K+1, p, fact, invfact)
if __name__ == '__main__':
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    outputs = []
    for _ in range(t):
        N = int(data[idx]); idx += 1
        K = int(data[idx]); idx += 1
        p = int(data[idx]); idx += 1
        outputs.append(str(solve(N, K, p)))

    print("\n".join(outputs))