import numpy as np

# Read input
n, m = map(int, input().split())

# Read the 2-D array
arr = np.array([input().split() for _ in range(n)], dtype=int)

# Sum along axis 1
mean_result = np.mean(arr, axis=1)
var_result = np.var(arr, axis=0)
std_result = round(np.std(arr, axis= None), 11)


# Print the result
print(mean_result)
print(var_result)
print(std_result)
