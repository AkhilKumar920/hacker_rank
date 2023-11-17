from collections import deque

def can_stack_cubes(num_test_cases, test_cases):
    results = []
    for _ in range(num_test_cases):
        _, cube_sizes = test_cases[_]
        cube_stack = deque(cube_sizes)
        last_cube = float('inf')
        while cube_stack:
            left, right = cube_stack[0], cube_stack[-1]
            if left >= right and left <= last_cube:
                last_cube = cube_stack.popleft()
            elif right > left and right <= last_cube:
                last_cube = cube_stack.pop()
            else:
                results.append("No")
                break
        else:
            results.append("Yes")
    return results

# Read the number of test cases
num_test_cases = int(input())

# Read the test cases
test_cases = []
for _ in range(num_test_cases):
    _ = int(input())
    cube_sizes = list(map(int, input().split()))
    test_cases.append((_, cube_sizes))

# Check if it is possible to stack the cubes for each test case
results = can_stack_cubes(num_test_cases, test_cases)

# Print the results
for result in results:
    print(result)
