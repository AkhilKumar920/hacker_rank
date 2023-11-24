#!/bin/python3

import math
import os
import random
import re
import sys


def greatest_product(num, k):
    max_product = 0
    for i in range(len(num) - k + 1):
        product = 1
        for j in range(i, i + k):
            product *= int(num[j])
        max_product = max(max_product, product)
    return max_product


if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        num = input().strip()

        # Calculate and print the greatest product
        result = greatest_product(num, k)
        print(result)
