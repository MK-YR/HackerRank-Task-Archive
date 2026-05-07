#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twosCompliment' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER a
#  2. LONG_INTEGER b
#
BITS = 32
MASK = 0xFFFFFFFF
def count_bits(n):
    if n < 0:
        return 0
    total = 0
    bit = 0
    while (1 << bit) <= n:
        cycle = 1 << (bit + 1)
        full_cycles = (n + 1) // cycle
        total += full_cycles * (1 << bit)
        remainder = (n + 1) % cycle
        total += max(0, remainder - (1 << bit))
        bit += 1
    return total
def range_bits(l, r):
    return count_bits(r) - count_bits(l - 1)
def twosCompliment(a, b):
    ua = a & MASK
    ub = b & MASK
    if ua <= ub:
        return range_bits(ua, ub)
    return (
        range_bits(ua, MASK)
        + range_bits(0, ub)
    )
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = twosCompliment(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
