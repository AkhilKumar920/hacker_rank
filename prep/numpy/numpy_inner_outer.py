import numpy as np

# Read input
A = np.array(input().split(), dtype=int)
B = np.array(input().split(), dtype=int)

# Compute the inner product
inner_product = np.inner(A, B)

# Compute the outer product
outer_product = np.outer(A, B)

# Print the results
print(inner_product)
print(outer_product)
