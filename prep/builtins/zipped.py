(n, x) = map(int, input().split(" "))
marks = []
for i in range(x):
    sub = [map(float, input().split(" "))]
    marks += sub
zipped = zip(*marks)
for i in zipped:
    print(sum(i)/x)

