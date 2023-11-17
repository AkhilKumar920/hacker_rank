from collections import OrderedDict


def word_occurrences(n, words):
    word_count = OrderedDict()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    distinct_words_count = len(word_count)
    occurrences = list(word_count.values())

    print(distinct_words_count)
    print(*occurrences)


# Read input
n = int(input().strip())
words = [input().strip() for _ in range(n)]

# Call the function and print the output
word_occurrences(n, words)
