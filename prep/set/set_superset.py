# Get the elements of set A
set_A = set(map(int, input().split()))

# Get the number of other sets
num_sets = int(input())

# Initialize a flag to check strict superset
is_strict_superset = True

# Process each set and check if set A is a strict superset
for _ in range(num_sets):
    other_set = set(map(int, input().split()))
    if not set_A.issuperset(other_set) or set_A == other_set:
        is_strict_superset = False
        break

# Print the result
print(is_strict_superset)
