from collections import deque


def perform_operations(operations):
    d = deque()

    for op in operations:
        operation, *values = op.split()
        if hasattr(d, operation):
            getattr(d, operation)(*map(int, values))

    print(*d)


# Read the number of operations
n = int(input().strip())

# Read the operations and their values
operations = [input().strip() for _ in range(n)]

# Perform the operations and print the result
perform_operations(operations)
