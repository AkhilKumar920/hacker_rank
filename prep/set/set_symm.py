# Get the number of students subscribed to the English newspaper
n = int(input())
english_subscribers = set(map(int, input().split()))

# Get the number of students subscribed to the French newspaper
m = int(input())
french_subscribers = set(map(int, input().split()))

# Find the students subscribed to either English or French but not both
exclusive_subscribers = (english_subscribers.symmetric_difference(french_subscribers))

# Print the total number of students with subscriptions to either English or French, but not both
print(len(exclusive_subscribers))
