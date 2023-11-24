n , list= int(input()), input().split(" ")
print(any([i == i[::-1] for i in list])) if all([int(x) > 0 for x in list]) else print(False)


