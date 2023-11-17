from itertools import combinations as cb
inpt = input().split(" ")
srtd = "".join(sorted(inpt[0]))
cmbs = []
for i in range(1,int(inpt[1])+1):
    cmbs += list(cb(srtd, i))
# for i in srtd:
#     print(i)
for i in cmbs:
    print("".join(i))