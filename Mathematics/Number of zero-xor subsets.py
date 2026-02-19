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
# The function accepts LONG_INTEGER n as parameter.
#

def solve(n):
    MOD = 10**9 + 7
    PHI = MOD - 1  #Fermat reduction for exponent
    pow2N_mod = pow(2, n, PHI)
    E = (pow2N_mod - (n % PHI)) % PHI
    return pow(2, E, MOD)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)

        fptr.write(str(result) + '\n')

    fptr.close()
