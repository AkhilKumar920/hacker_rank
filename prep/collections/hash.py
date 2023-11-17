s = input()
alnum = False
alpha = False
digit = False
lcase = False
ucase = False
for i in s:
    if i.isalnum():
        alnum = True
    if i.isalpha():
        alpha = True
    if i.isdigit():
        digit = True
    if i.islower():
        lcase = True
    if i.isupper():
        ucase = True
print(alnum)
print(alpha)
print(digit)
print(lcase)
print(ucase)