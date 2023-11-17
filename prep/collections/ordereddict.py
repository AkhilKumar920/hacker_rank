from collections import OrderedDict


def calculate_net_price(items):
    net_price_dict = OrderedDict()

    for item in items:
        item_name, price = item.rsplit(' ', 1)
        price = int(price)

        if item_name in net_price_dict:
            net_price_dict[item_name] += price
        else:
            net_price_dict[item_name] = price

    for item_name, net_price in net_price_dict.items():
        print(item_name, net_price)

# Read input
n = int(input().strip())
items = [input().strip() for _ in range(n)]

# Call the function and print the output
calculate_net_price(items)
