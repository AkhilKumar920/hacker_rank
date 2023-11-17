import numpy as np

# Read input
n, m = map(int, input().split())

# Read the 2-D array
arr = np.array([input().split() for _ in range(n)], dtype=int)

# Sum along axis 1
sum_result = np.sum(arr, axis=0)

# Find the product of the sum
product_result = np.prod(sum_result)

# Print the result
print(product_result)
