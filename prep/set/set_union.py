# Get the number of students subscribed to the English newspaper
n = int(input())
english_subscribers = set(map(int, input().split()))

# Get the number of students subscribed to the French newspaper
m = int(input())
french_subscribers = set(map(int, input().split()))

# Find the total number of students with at least one subscription
total_subscribers = len(english_subscribers.union(french_subscribers))

# Print the result
print(total_subscribers)
