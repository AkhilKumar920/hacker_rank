def find_pythagorean_triplet_product(n):
    max_product = -1

    # Iterate through possible values of a
    for a in range(1, n // 3):
        b = (n * (n - 2 * a)) // (2 * (n - a))

        # Check if a, b, and c form a Pythagorean triplet
        if a**2 + b**2 == (n - a - b)**2:
            product = a * b * (n - a - b)
            max_product = max(max_product, product)

    return max_product


if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())

        # Find and print the maximum possible product for each test case
        result = find_pythagorean_triplet_product(n)
        print(result)
