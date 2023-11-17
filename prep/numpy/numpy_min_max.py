import numpy as np

# Read input
n, m = map(int, input().split())

# Read the 2-D array
arr = np.array([input().split() for _ in range(n)], dtype=int)

# Sum along axis 1
min_result = np.min(arr, axis=1)

# Find the product of the sum
max_result = np.max(min_result)

# Print the result
print(max_result)
