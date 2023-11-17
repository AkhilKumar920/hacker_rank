from collections import defaultdict

def word_positions(n, m, group_a, group_b):
    positions = defaultdict(list)

    # Store positions of words in group A
    for i in range(n):
        positions[group_a[i]].append(i + 1)

    # Check and print positions of words in group B
    for word in group_b:
        if word in positions:
            print(*positions[word])
        else:
            print(-1)

# Read input
n, m = map(int, input().split())
group_a = [input().strip() for _ in range(n)]
group_b = [input().strip() for _ in range(m)]

# Call the function and print the output
word_positions(n, m, group_a, group_b)
