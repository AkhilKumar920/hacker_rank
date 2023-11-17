def merge_the_tools(string, k):
    n = len(string)

    for i in range(0, n, k):
        sub_string = string[i:i+k]
        unique_chars = []
        for char in sub_string:
            if char not in unique_chars:
                unique_chars.append(char)
        print("".join(unique_chars))


if __name__ == '__main__':
    string = input()
    k = int(input())
    merge_the_tools(string, k)