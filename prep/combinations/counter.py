shoe_count = int(input())
sizes = input().split(" ")
shoe_sizes = []
for i in sizes:
    shoe_sizes += [int(i)]
customers = int(input())
total_earned = 0
for i in range(customers):
    desired_size_price = input().split(" ")
    desired_size = int(desired_size_price[0])
    desired_price = int(desired_size_price[1])
    if desired_size in shoe_sizes:
        total_earned += desired_price
        shoe_sizes.remove(desired_size)
print(total_earned)