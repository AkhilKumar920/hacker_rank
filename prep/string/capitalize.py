def solve(inpt):
    lst = inpt.split(" ")
    x = []
    for i in lst:
        x += [i.capitalize()]
    print(" ".join(x))


s = input()

solve(s)