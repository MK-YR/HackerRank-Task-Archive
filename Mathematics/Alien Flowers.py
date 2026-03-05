#!/bin/python3

import math
import os
import random
import re
import sys

MOD = 10**9 + 7
MAX = 200005
fact = [1]*MAX
invfact = [1]*MAX
for i in range(1, MAX):
    fact[i] = fact[i-1]*i % MOD
invfact[MAX-1] = pow(fact[MAX-1], MOD-2, MOD)
for i in range(MAX-2, -1, -1):
    invfact[i] = invfact[i+1]*(i+1) % MOD
def comb(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n]*invfact[r]%MOD*invfact[n-r]%MOD
def count(startR, A, B, C, D):
    k = B + D
    blocks = k + 1
    if startR:
        r_blocks = (k + 2)//2
        b_blocks = blocks - r_blocks
    else:
        b_blocks = (k + 2)//2
        r_blocks = blocks - b_blocks
    return comb(A + r_blocks - 1, r_blocks - 1) * comb(C + b_blocks - 1, b_blocks - 1) % MOD
if __name__ == '__main__':
    A, B, C, D = map(int, input().split())
    if B == 0 and D == 0:
        if A > 0 and C > 0:
            print(0)
        elif A > 0:
            print(1)
        elif C > 0:
            print(1)
        else:
            print(2)
        sys.exit()
    ans = 0
    if B == D:
        ans = (count(True, A, B, C, D) + count(False, A, B, C, D)) % MOD
    elif B == D + 1:
        ans = count(True, A, B, C, D)
    elif D == B + 1:
        ans = count(False, A, B, C, D)
    print(ans % MOD)
