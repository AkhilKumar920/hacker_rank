# Get the number of elements in the set
n = int(input())

# Create the set with non-negative integers less than or equal to 9
s = set(map(int, input().split()))

# Get the number of commands
num_commands = int(input())

# Execute the commands
for _ in range(num_commands):
    command = input().split()

    # Check the type of command and execute accordingly
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        s.remove(int(command[1]))
    elif command[0] == 'discard':
        s.discard(int(command[1]))

# Print the sum of the elements in the set
print(sum(s))
