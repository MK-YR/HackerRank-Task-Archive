#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x
#  2. INTEGER y
#  3. INTEGER k
#

#!/bin/python3

def find_next_step(h, v, k):
    result = []
    while h > 0 or v > 0:
        if h == 0:
            result.append('V')
            v -= 1
        elif v == 0:
            result.append('H')
            h -= 1
        else:
            count = math.comb(h + v - 1, h - 1)

            if count > k:
                result.append('H')
                h -= 1
            else:
                result.append('V')
                k -= count
                v -= 1
    return ''.join(result)
def main():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        h, v, k = map(int, sys.stdin.readline().split())
        print(find_next_step(h, v, k))
if __name__ == "__main__":
    main()