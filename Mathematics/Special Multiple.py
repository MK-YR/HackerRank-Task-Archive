# You are given an integer N. Can you find the least positive integer X made up of only 9's and 0's, such that, X is a multiple of N?
#
# Update
#
# X is made up of one or more occurences of 9 and zero or more occurences of 0.
#
# Input Format
# The first line contains an integer T which denotes the number of test cases. T lines follow.
# Each line contains the integer N for which the solution has to be found.
#
# Output Format
# Print the answer X to STDOUT corresponding to each test case. The output should not contain any leading zeroes.
#
# Constraints
# 1 <= T <= 104
# 1 <= N <= 500
#
# Sample Input
#
# 3
# 5
# 7
# 1
# Sample Output
#
# 90
# 9009
# 9
# Explanation
# 90 is the smallest number made up of 9's and 0's divisible by 5. Similarly, you can derive for other cases.
#
# Timelimits Timelimits for this challenge is given here

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#
def solve(n):
    if n == 1:
        return "9"
    queue = deque()
    queue.append(("9", 9 % n))
    visited = set()
    visited.add(9 % n)
    while queue:
        num_str, remainder = queue.popleft()
        if remainder == 0:
            return num_str
        next_rem = (remainder * 10) % n
        if next_rem not in visited:
            queue.append((num_str + "0", next_rem))
            visited.add(next_rem)
        next_rem = (remainder * 10 + 9) % n
        if next_rem not in visited:
            queue.append((num_str + "9", next_rem))
            visited.add(next_rem)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()