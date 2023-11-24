s = input()
lower = ""
upper = ""
odd = ""
even = ""
for i in s:
    if i.islower():
        lower += i
    if i.isupper():
        upper += i
    if i.isdigit():
        if int(i) % 2 == 0:
            even += i
        else:
            odd += i
sorted = sorted(lower) + sorted(upper) + sorted(odd) + sorted(even)
print("".join(sorted))

