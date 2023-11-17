import cmath

def convert_to_polar(complex_num):
    polar_coordinates = cmath.polar(complex_num)
    return polar_coordinates

# Read input
input_complex = complex(input().strip())

# Convert to polar coordinates
polar_coordinates = convert_to_polar(input_complex)

# Print the values with 3 decimal places
print(round(polar_coordinates[0], 3))
print(round(polar_coordinates[1], 3))
