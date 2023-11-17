# Get the number of students subscribed to the English newspaper
n = int(input())
english_subscribers = set(map(int, input().split()))

# Get the number of students subscribed to the French newspaper
m = int(input())
french_subscribers = set(map(int, input().split()))

# Find the students subscribed only to the English newspaper
english_only_subscribers = english_subscribers.difference(french_subscribers)

# Print the total number of students with English-only subscriptions
print(len(english_only_subscribers))
