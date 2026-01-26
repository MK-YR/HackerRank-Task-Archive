#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    freq = Counter(s)  #Count each character
    freq_counts = Counter(freq.values())  #Count frequency of frequencies
    if len(freq_counts) == 1:
        return "YES"
    if len(freq_counts) == 2:
        key1, key2 = freq_counts.keys()
        val1, val2 = freq_counts[key1], freq_counts[key2]
        if (val1 == 1 and key1 == 1) or (val2 == 1 and key2 == 1):
            return "YES"
        if (val1 == 1 and key1 - key2 == 1) or (val2 == 1 and key2 - key1 == 1):
            return "YES"
    return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
