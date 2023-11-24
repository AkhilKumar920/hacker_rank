import re


def is_valid_uid(uid):
    return bool(re.match(r'^(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})[a-zA-Z0-9]{10}$', uid))


# Input: Number of test cases
t = int(input().strip())

# Process each test case
for _ in range(t):
    # Input: Employee's UID
    uid = input().strip()

    # Output: Print 'Valid' or 'Invalid'
    print('Valid' if is_valid_uid(uid) else 'Invalid')


# Working in hackerrank:
# def is_valid_uid(uid):
#     # Rule 1: At least 2 uppercase English alphabet characters
#     if sum(c.isupper() for c in uid) < 2:
#         return False
#
#     # Rule 2: At least 3 digits
#     if sum(c.isdigit() for c in uid) < 3:
#         return False
#
#     # Rule 3: Only alphanumeric characters and no repeats
#     if len(set(uid)) != len(uid):
#         return False
#
#     # Rule 4: Exactly 10 characters in a valid UID
#     if len(uid) != 10:
#         return False
#
#     return True
#
# # Input: Number of test cases
# t = int(input().strip())
#
# # Process each test case
# for _ in range(t):
#     # Input: Employee's UID
#     uid = input().strip()
#
#     # Output: Print 'Valid' or 'Invalid'
#     if is_valid_uid(uid):
#         print('Valid')
#     else:
#         print('Invalid')

