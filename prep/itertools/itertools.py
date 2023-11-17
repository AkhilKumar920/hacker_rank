from itertools import product
x = map(int, input().split(" "))
y = map(int, input().split(" "))
z = map(str, list(product(x, y)))
op = " ".join(z)
print(op)