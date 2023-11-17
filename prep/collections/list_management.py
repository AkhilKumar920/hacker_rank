# list = []
n = int(input())
cmnd = []
final_list = []
for i in range(n):
    cmnd += [input().split(" ")]
for i in range(n):
    cmd = cmnd[i]
    if cmd[0] == "insert":
        final_list.insert(int(cmd[1]), int(cmd[2]))
    if cmd[0] == "print":
        print(final_list)
    if cmd[0] == "remove":
        final_list.remove(int(cmd[1]))
    if cmd[0] == "append":
        final_list.append(int(cmd[1]))
    if cmd[0] == "sort":
        final_list.sort()
    if cmd[0] == "pop":
        final_list.pop()
    if cmd[0] == "reverse":
        final_list.reverse()

