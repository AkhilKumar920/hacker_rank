import numpy as np

# Read input
n = int(input().strip())

# Read array A
A = np.array([input().split() for _ in range(n)], dtype=int)

# Read array B
B = np.array([input().split() for _ in range(n)], dtype=int)

# Compute the matrix product
result = np.dot(A, B)

# Print the result
print(result)
