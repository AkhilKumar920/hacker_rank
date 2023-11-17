def rangoli(size):
    import string

    alphabet = string.ascii_lowercase
    lines = []

    for i in range(size):
        s = '-'.join(alphabet[size - 1:i:-1] + alphabet[i:size])
        line = (s.center(size * 4 - 3, '-'))
        lines.append(line)

    print('\n'.join(lines[::-1] + lines[1:]))


# Sample Input
size = int(input().strip())

# Sample Output
rangoli(size)

