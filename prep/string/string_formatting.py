def print_formatted(number):
    width = len(bin(number)[2:])

    for i in range(1, number + 1):
        decimal_value = str(i).rjust(width)
        octal_value = oct(i)[2:].rjust(width)
        hexadecimal_value = hex(i)[2:].upper().rjust(width)
        binary_value = bin(i)[2:].rjust(width)

        print(f"{decimal_value} {octal_value} {hexadecimal_value} {binary_value}")

# Sample Input
number = int(input().strip())

# Sample Output
print_formatted(number)