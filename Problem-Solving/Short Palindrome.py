#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'shortPalindrome' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def shortPalindrome(s):
    MOD = 10**9 + 7
    arr1 = [0] * 26
    arr2 = [[0] * 26 for _ in range(26)]
    arr3 = [0] * 26
    ans = 0
    for char in s:
        idx = ord(char) - ord('a')
        ans = (ans + arr3[idx]) % MOD
        for j in range(26):
            arr3[j] = (arr3[j] + arr2[j][idx]) % MOD
        for j in range(26):
            arr2[j][idx] = (arr2[j][idx] + arr1[j]) % MOD
        arr1[idx] = (arr1[idx] + 1) % MOD
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = shortPalindrome(s)

    fptr.write(str(result) + '\n')

    fptr.close()
