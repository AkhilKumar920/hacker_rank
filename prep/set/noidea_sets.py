n = input().split()
a_n = int(n[0])
b_c_n = int(n[1])
arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

happiness = 0

for num in arr:
    if num in a:
        happiness += 1
    elif num in b:
        happiness -= 1

print(happiness)
