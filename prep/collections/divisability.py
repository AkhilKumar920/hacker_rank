def is_divisible_by_k(n, arr):
    # Get the last digit of each number in the array
    last_digits = [str(x)[-1] for x in arr]

    # Form the number using the last digits
    formed_number = int("".join(last_digits))

    # Check if the formed number is divisible by k
    if formed_number % n == 0:
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    # Input reading
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))

    # Output the result
    result = is_divisible_by_k(n, arr)
    print(result)





