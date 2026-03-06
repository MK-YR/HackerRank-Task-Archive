#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridlandMetro' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER k
#  4. 2D_INTEGER_ARRAY track
#

def gridlandMetro(n, m, k, track):
    from collections import defaultdict
    tracks_by_row = defaultdict(list)
    for r, c1, c2 in track:
        tracks_by_row[r].append((c1, c2))
    total_track_cells = 0
    for row in tracks_by_row:
        intervals = sorted(tracks_by_row[row])
        merged = []
        for start, end in intervals:
            if not merged:
                merged.append([start, end])
            else:
                last_start, last_end = merged[-1]
                if start <= last_end + 1:
                    merged[-1][1] = max(last_end, end)
                else:
                    merged.append([start, end])
        for s, e in merged:
            total_track_cells += e - s + 1
    return n * m - total_track_cells
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')

    fptr.close()
