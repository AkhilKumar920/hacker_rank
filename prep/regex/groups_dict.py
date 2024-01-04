import re

def find_repeating_character(s):
    # Define a regular expression pattern to find alphanumeric repeating characters
    pattern = r'([a-zA-Z0-9])\1+'

    # Use re.search to find the first occurrence of the pattern
    match = re.search(pattern, s)

    # Check if a match is found
    if match:
        # Return the first repeating alphanumeric character
        return match.group(1)
    else:
        # No repeating character found
        return -1

# Input the string
input_string = input().strip()

# Find and print the result
result = find_repeating_character(input_string)
print(result)
