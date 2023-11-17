def is_palindrome(num):
    return str(num) == str(num)[::-1]


def largest_palindrome(limit):
    max_palindrome = 0
    for i in range(999, 99, -1):
        for j in range(999, i - 1, -1):
            product = i * j
            if product < limit and is_palindrome(product):
                max_palindrome = max(max_palindrome, product)
    return max_palindrome


t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    result = largest_palindrome(n)
    print(result)
