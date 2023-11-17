from itertools import permutations as pt
inpt = input().split(" ")
word = list(inpt[0])
no = int(inpt[1])
perm = list(pt(word, no))
perm.sort()
for i in perm:
    print("".join(i))
