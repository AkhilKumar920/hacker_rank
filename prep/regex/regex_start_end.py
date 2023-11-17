import re

# Get the input strings
string = input()
substring = input()

# Define the regex pattern for finding the substring
pattern = re.compile(f'(?=({substring}))')

# Find all occurrences of the substring in the string
matches = re.finditer(pattern, string)

# Print the indices of the start and end of each match
for match in matches:
    print((match.start(1), match.end(1) - 1))

# If no match is found, print (-1, -1)
if not re.search(pattern, string):
    print((-1, -1))
