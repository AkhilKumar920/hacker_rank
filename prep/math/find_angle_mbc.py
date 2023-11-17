import math


def find_angle(AB, BC):
    angle = math.degrees(math.atan2(AB, BC))
    return round(angle)


# Read input
AB = float(input().strip())
BC = float(input().strip())

# Find and print the angle in degrees
result = find_angle(AB, BC)
print(f"{result}°")
