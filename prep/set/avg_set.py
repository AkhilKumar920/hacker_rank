def average(array):
    # your code goes here
    total = 0
    for i in set(array):
        total += i
    return round(total / len(set(array)), 3)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

