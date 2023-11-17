#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'mostBalancedPartition' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY parent
#  2. INTEGER_ARRAY files_size
#
def dfs(node, adj_list, files_size, subtree_sizes):
    size = files_size[node]
    for child in adj_list[node]:
        size += dfs(child, adj_list, files_size, subtree_sizes)
        subtree_sizes[node] = size
    return size
def mostBalancedPartition(parent, files_size):
    # Write your code here
    n = len(parent)

    adj_list = {i: [] for i in range(n)}
    for i, p in enumerate(parent):
        if p != -1:
            adj_list[p].append(i)


    subtree_sizes = [0] * n
    dfs(0, adj_list, files_size, subtree_sizes)

    total_size = subtree_sizes[0]

    min_diff = float("inf")
    for i in range(1, n):
        diff = abs(total_size - 2 * subtree_sizes[i])
        min_diff = min(min_diff, diff)
    return min_diff
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    parent_count = int(input().strip())

    parent = []

    for _ in range(parent_count):
        parent_item = int(input().strip())
        parent.append(parent_item)

    files_size_count = int(input().strip())

    files_size = []

    for _ in range(files_size_count):
        files_size_item = int(input().strip())
        files_size.append(files_size_item)

    result = mostBalancedPartition(parent, files_size)

    fptr.write(str(result) + '\n')

    fptr.close()
