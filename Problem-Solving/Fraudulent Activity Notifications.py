#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def get_twice_median(count, d):
    if d % 2 == 1:
        target = d // 2 + 1
        cumulative = 0
        for value in range(201):
            cumulative += count[value]
            if cumulative >= target:
                return 2 * value
    else:
        first = d // 2
        second = first + 1
        cumulative = 0
        median1 = None
        median2 = None
        for value in range(201):
            cumulative += count[value]
            if median1 is None and cumulative >= first:
                median1 = value
            if cumulative >= second:
                median2 = value
                break
        return median1 + median2
def activityNotifications(expenditure, d):
    notifications = 0
    count = [0] * 201
    for i in range(d):
        count[expenditure[i]] += 1
    for i in range(d, len(expenditure)):
        twice_median = get_twice_median(count, d)
        if expenditure[i] >= twice_median:
            notifications += 1
        old_value = expenditure[i - d]
        count[old_value] -= 1
        new_value = expenditure[i]
        count[new_value] += 1
    return notifications
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
