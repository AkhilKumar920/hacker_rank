from itertools import groupby


def compress_string(s):
    compressed = []
    for key, group in groupby(s):
        count = len(list(group))
        compressed.append((count, int(key)))

    result = ' '.join(['({}, {})'.format(count, key) for count, key in compressed])
    return result


# Sample Input
input_string = input()

# Output
output_string = compress_string(input_string)
print(output_string)
