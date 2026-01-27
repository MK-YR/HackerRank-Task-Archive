# The Indian bank issues coins in 4 denominations, ₹1, ₹2, ₹5 and ₹10.
#
# Given a limited supply of each of the above denominations, in how many ways can you sum them up to a total of ₹N?
#
# Input Format
# The first line contains an integer T (number of testcases). Each testcase contains 2 lines. The first line contains integer N (sum to be achieved)
# A, B, C and D in the next line, each representing the number of ₹1, ₹2, ₹5 and ₹10 coins respectively.
#
# Output Format
# Output the number of ways in which we can achieve the sum N.
#
# Constraints
# 1 <= T <= 150
# 1 <= N <= 1000
# 1 <= A <= 10000
# 1 <= B,C,D <= 1000
#
# Sample Input
#
# 2
# 15
# 2 3 1 1
# 12
# 2 2 1 1
# Sample Output
#
# 2
# 2
# Explanation
# In the first case we need to find the different ways to total to 15. We can use one ₹10 coin and one ₹5 coin or one ₹10 coin two ₹2 coin and one ₹1 coin. Proceed similarly for the second case.

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
#  2. INTEGER_ARRAY coins
#

def solve(n, coins):
    A, B, C, D = coins
    count = 0
    for w in range(min(D, n // 10) + 1): #10 coins
        rem1 = n - 10 * w
        for z in range(min(C, rem1 // 5) + 1): #5 coins
            rem2 = rem1 - 5 * z
            for y in range(min(B, rem2 // 2) + 1): #2 coins
                rem3 = rem2 - 2 * y
                if rem3 <= A: #Rem3 must be paid using 1 coins
                    count += 1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        coins = list(map(int, input().rstrip().split()))

        result = solve(n, coins)

        fptr.write(str(result) + '\n')

    fptr.close()
