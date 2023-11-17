t = int(input().strip())

for _ in range(t):
    n = int(input().strip())

    # Function to find the sum of multiples of 3 or 5 below a given number
    def sum_multiples(limit, divisor):
        limit -= 1  # Adjusting for "below" the given number
        num_divisors = limit // divisor
        return divisor * (num_divisors * (num_divisors + 1)) // 2

    # Calculate the sum for multiples of 3 and 5 and subtract the common multiples
    sum_3 = sum_multiples(n, 3)
    sum_5 = sum_multiples(n, 5)
    sum_15 = sum_multiples(n, 15)
    total_sum = sum_3 + sum_5 - sum_15

    print(total_sum)
