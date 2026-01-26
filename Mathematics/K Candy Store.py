# Jim enters a candy shop which has N different types of candies, each candy is of the same price. Jim has enough money to buy K candies. In how many different ways can he purchase K candies if there are infinite candies of each kind?
#
# Input Format
# The first line contains an integer T, the number of tests.
# This is followed by 2T lines which contain T tests:
# The first line (of each testcase) is an integer N and the second line (of each testcase) is an integer K.
#
# Output Format
# For each testcase, print the number of ways Jim can buy candies from the shop in a newline. If the answer has more than 9 digits, print the last 9 digits.
#
# Note
# This problem may expect you to have solved nCr Table
#
# Constraints
# 1 <= T <= 200
# 1 <= N < 1000
# 1 <= K < 1000
#
# Sample Input
#
# 2
# 4
# 1
# 2
# 3
# Sample Output
#
# 4
# 4
# Explanation
# There are 2 testcases, for the first testcase we have N = 4 and K = 1, as Jim can buy only 1 candy, he can choose to buy any of the 4 types of candies available. Hence, his answer is 4. For the 2nd testcase, we have N = 2 and K = 3, If we name two chocolates as a and b, he can buy
#
# aaa bbb aab abb
# chocolates, hence 4.

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
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

MOD = 10**9
MAX = 2000
nCr = [[0] * (MAX + 1) for _ in range(MAX + 1)] #Precompute nCr table
for i in range(MAX + 1):
    nCr[i][0] = 1
    for j in range(1, i + 1):
        if j == i:
            nCr[i][j] = 1
        else:
            nCr[i][j] = (nCr[i - 1][j - 1] + nCr[i - 1][j]) % MOD
def solve(n, k):
    return nCr[n + k - 1][k]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        k = int(input().strip())
        fptr.write(str(solve(n, k)) + "\n")
    fptr.close()