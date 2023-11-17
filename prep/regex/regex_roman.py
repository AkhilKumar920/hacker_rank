import re


def is_valid_roman(s):
    regex_pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    return bool(re.match(regex_pattern, s))


# Read input
roman_numeral = input()

# Check if it's a valid Roman numeral and print the result
print(is_valid_roman(roman_numeral))
