import re


def fun(s):
    if '@' in s and '.' in s and s.count('@') == 1 and s.count('.') == 1 and s.index('@') < s.index('.'):
        user_name = s.split("@")[0]
        website = (s.split("@")[1]).split(".")[0]
        extension = (s.split("@")[1]).split(".")[1]
        username_match = re.compile(r'[a-zA-Z0-9-_]*$')
        if len(user_name)>0 and username_match.match(user_name) and website.isalnum() and extension.isalpha() and len(extension) <= 3:
            return True
        else:
            return False


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

# Simplified solution:
# import sys, re
# n = int(input())
# a = [input() for i in range(n)]
# print(sorted([s.strip() for s in a if re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]{1,3}$', s)]))
