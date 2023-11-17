from collections import Counter as cnt
n = int(input())
room_no = input().split()
x = cnt(room_no)
for i in x.keys():
    if x[i] == 1:
        print(i)