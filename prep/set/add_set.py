# Get the total number of country stamps
n = int(input())

# Initialize an empty set to store distinct country stamps
distinct_stamps = set()

# Iterate through the input to add stamps to the set
for _ in range(n):
    country_stamp = input()
    distinct_stamps.add(country_stamp)

# Print the total number of distinct country stamps
print(len(distinct_stamps))
