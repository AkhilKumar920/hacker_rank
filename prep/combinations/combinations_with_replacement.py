from itertools import combinations_with_replacement as cmbt_rc
inpt = input().split(" ")
srtd = cmbt_rc("".join(sorted(inpt[0])), int(inpt[1]))
for i in srtd:
    print("".join(i))