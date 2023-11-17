import numpy as np

# Read input
coefficients = list(map(float, input().split()))
x_value = float(input().strip())

# Calculate the value of the polynomial at the given point
result = np.polyval(coefficients, x_value)

# Print the result
print(result)
