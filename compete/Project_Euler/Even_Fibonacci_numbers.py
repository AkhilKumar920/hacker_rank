t = int(input().strip())

for _ in range(t):
    n = int(input().strip())

    # Function to generate Fibonacci sequence and calculate sum of even terms
    def even_fibonacci_sum(limit):
        a, b = 1, 2
        even_sum = 0

        while b <= limit:
            if b % 2 == 0:
                even_sum += b

            a, b = b, a + b

        return even_sum

    result = even_fibonacci_sum(n)
    print(result)
