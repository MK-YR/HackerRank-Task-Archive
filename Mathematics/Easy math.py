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
# The function accepts INTEGER x as parameter.
#

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
# The function accepts INTEGER x as parameter.
#

def solve(x):
    n = x
    n2 = 0
    while x % 2 == 0:
        n2 += 1
        x //= 2
    n5 = 0
    while x % 5 == 0:
        n5 += 1
        x //= 5
    y = 1
    a = 1
    while y % x != 0:
        y = (y * 10 + 1) % x
        a += 1
    b = n5
    if n2 - n5 > 2:
        b += n2 - n5 - 2
    return 2 * a + b
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        x = int(input().strip())
        result = solve(x)
        fptr.write(str(result) + '\n')

    fptr.close()
