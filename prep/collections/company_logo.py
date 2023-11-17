if __name__ == '__main__':
    s = input()
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    sorted_char_count = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))

    for i in range(3):
        char, count = sorted_char_count[i]
        print(f"{char} {count}")
