import re


def is_valid_regex(x):
    try:
        re.compile(x)
        return True
    except re.error:
        return False


# Input reading
t = int(input())

for _ in range(t):
    pattern = input()
    result = is_valid_regex(pattern)
    print(result)
