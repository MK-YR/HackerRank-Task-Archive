#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    moves = 0
    while n != 1:
        if (n & (n - 1)) == 0:
            n >>= 1
        else:
            n -= 1 << (n.bit_length() - 1)
        moves += 1
    if moves % 2 == 1:
        return "Louise"
    else:
        return "Richard"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()