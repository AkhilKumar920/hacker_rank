from prep.itertools import combinations

def calculate_probability(n, elements, k):
    total_combinations = list(combinations(elements, k))
    combinations_without_a = [c for c in total_combinations if 'a' not in c]

    probability_without_a = len(combinations_without_a) / len(total_combinations)
    probability_with_a = 1 - probability_without_a

    return round(probability_with_a, 4)

# Read input
n = int(input())
elements = input().split()
k = int(input())

# Calculate and print the probability
result = calculate_probability(n, elements, k)
print(result)
