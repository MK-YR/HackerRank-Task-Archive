#!/bin/python3

import math
import os
import random
import re
import sys

def evenForest(t_nodes, t_edges, t_from, t_to):
    from collections import defaultdict
    graph = defaultdict(list)
    for u, v in zip(t_from, t_to):
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * (t_nodes + 1)
    removable = 0
    def dfs(node):
        nonlocal removable
        visited[node] = True
        subtree_size = 1
        for neighbor in graph[node]:
            if not visited[neighbor]:
                child_size = dfs(neighbor)
                if child_size % 2 == 0:
                    removable += 1
                else:
                    subtree_size += child_size
        return subtree_size
    dfs(1)
    return removable
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
