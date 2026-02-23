#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price):
    n = len(price)
    prices = [(price[i], i) for i in range(n)]
    prices.sort()
    min_loss = float('inf')
    for i in range(1, n):
        price1, year1 = prices[i-1]
        price2, year2 = prices[i]
        if year1 > year2:
            loss = price2 - price1
            if loss < min_loss:
                min_loss = loss
    return min_loss
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
