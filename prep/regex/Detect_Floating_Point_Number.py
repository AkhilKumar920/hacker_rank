import re

def is_valid_float(s):
    # Define the regular expression pattern for a valid float
    pattern = r'^[+-]?(\d*\.\d+|\d+\.\d*)$'

    # Use re.match to check if the string matches the pattern
    match = re.match(pattern, s)

    # Check for specific conditions
    if not match:
        return False
    if s.count('.') != 1:
        return False  # Must have exactly one '.' symbol
    if s[0] in ['+', '-'] and s[1] == '.':
        return True  # Number can start with +, - or ., but not with -+
    if s[-1] == '.':
        return False  # Must contain at least one decimal value

    return True


# Input the number of test cases
t = int(input().strip())

# Iterate through each test case
for _ in range(t):
    # Input the string
    test_string = input().strip()

    # Check and print the result for each test case
    print(is_valid_float(test_string))
