import sys


def largest_prime_factor(num):
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
    return num


t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    result = largest_prime_factor(n)
    print(result)
