#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY n as parameter.
#

#!/bin/python3

MOD = 10**9 + 7
def solve(n):
    m = min(n)
    f = [0] * (m + 1)
    for g in range(m, 0, -1):
        total = 1
        for x in n:
            total = (total * (x // g)) % MOD
        k = 2 * g
        sub = 0
        while k <= m:
            sub = (sub + f[k]) % MOD
            k += g
        f[g] = (total - sub) % MOD
    ans = 0
    for g in range(1, m + 1):
        ans = (ans + g * f[g]) % MOD
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for _ in range(t):
        n_count = int(input().strip())
        n = list(map(int, input().rstrip().split()))
        result = solve(n)
        fptr.write(str(result) + '\n')
    fptr.close()