# Get the number of elements in set A
n = int(input())
set_A = set(map(int, input().split()))

# Get the number of other sets
num_other_sets = int(input())

# Perform mutation operations on set A
for _ in range(num_other_sets):
    operation_info = input().split()
    operation_name = operation_info[0]
    num_elements = int(operation_info[1])
    other_set = set(map(int, input().split()))

    # Perform the specified operation on set A
    if operation_name == "intersection_update":
        set_A.intersection_update(other_set)
    elif operation_name == "update":
        set_A.update(other_set)
    elif operation_name == "symmetric_difference_update":
        set_A.symmetric_difference_update(other_set)
    elif operation_name == "difference_update":
        set_A.difference_update(other_set)

# Print the sum of elements in set A
print(sum(set_A))
