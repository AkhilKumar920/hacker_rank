def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(limit):
    prime_sum = 0
    for num in range(2, limit + 1):
        if is_prime(num):
            prime_sum += num
    return prime_sum

if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())

        # Find and print the sum of primes up to the given limit
        result = sum_of_primes(n)
        print(result)
