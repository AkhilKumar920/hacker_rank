import re

# Get the input string
s = input()

# Define the regex pattern for finding substrings
pattern = re.compile(r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])[aeiouAEIOU]{2,}(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])')

# Find all the substrings matching the pattern
matches = re.findall(pattern, s)

# Print the matched substrings or -1 if no match is found
if matches:
    for match in matches:
        print(match)
else:
    print(-1)
