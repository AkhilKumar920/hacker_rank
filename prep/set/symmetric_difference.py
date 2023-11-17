a_n = int(input())
a = set(map(int, input().split()))
b_n = int(input())
b = set(map(int, input().split()))
x = []
x += a.difference(b)
x += b.difference(a)
for i in sorted(x):
    print(i)