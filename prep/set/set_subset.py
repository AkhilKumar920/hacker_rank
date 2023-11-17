# Get the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Get the elements of set A
    n_A = int(input())
    set_A = set(map(int, input().split()))

    # Get the elements of set B
    n_B = int(input())
    set_B = set(map(int, input().split()))

    # Check if set A is a subset of set B
    is_subset = set_A.issubset(set_B)

    # Print the result for each test case
    print(is_subset)
