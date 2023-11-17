def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i*i, limit + 1, i):
                primes[j] = False
    return [x for x in range(limit + 1) if primes[x]]


def nth_prime(n):
    primes = sieve_of_eratosthenes(110000)  # Adjust the limit based on the maximum n
    return primes[n - 1]


t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    result = nth_prime(n)
    print(result)
