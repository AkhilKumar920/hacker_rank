inpt = input().split(" ")
thickness = int((int(inpt[1]) - 3)/2)
c = '.|.'
x = int(int(inpt[0])/2)

for i in range(x):
    print((c*i).rjust(thickness,'-')+c+(c*i).ljust(thickness,'-'))
print("WELCOME".center(int(inpt[1]),'-'))
for i in range(x):
    print(((c*(x-i-1)).rjust(thickness,'-')+c+(c*(x-i-1)).ljust(thickness,'-')))