#!/bin/python3

import os
import sys

# Complete the solve function below.

def solve(a):
    fib = [1, 2]
    for _ in range(100): #Create Fibonacci sequence for Zeckendorf's theorem
        fib.append(fib[-2]+fib[-1])
    def get_zeck(n): #Converts each number into its unique Zeckendorf form and treats like binary
        ret = ''
        for f in reversed(fib):
            if n >= f:
                ret += '1'
                n -= f
            else:
                ret += '0'
        return ret.lstrip('0')
    result = 0
    for num in a:
        result ^= int(get_zeck(num), 2) #XOR
    return result % (10**9 + 7)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    fptr.write(str(result) + '\n')

    fptr.close()