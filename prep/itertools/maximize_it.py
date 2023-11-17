from itertools import product

def maximize_expression(arr, m):
    max_value = 0

    # Generate all possible combinations
    combinations = list(product(*arr))

    # Find the maximum value of the expression
    for combo in combinations:
        current_value = sum(x ** 2 for x in combo) % m
        max_value = max(max_value, current_value)

    return max_value

# Read input
n, m = map(int, input().split())
lists = [list(map(int, input().split()[1:])) for _ in range(n)]

# Find and print the result
result = maximize_expression(lists, m)
print(result)
