#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#

def generate_primes(q):
    primes = []
    num = 2
    while len(primes) < q:
        is_prime = True
        for p in primes:
            if p * p > num:
                break
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes
def waiter(number, q):
    primes = generate_primes(q)
    A = number[:]
    answer = []
    for prime in primes:
        next_A = []
        B = []
        while A:
            plate = A.pop()
            if plate % prime == 0:
                B.append(plate)
            else:
                next_A.append(plate)
        while B:
            answer.append(B.pop())
        A = next_A
    while A:
        answer.append(A.pop())
    return answer
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
