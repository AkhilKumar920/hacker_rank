cube = lambda x: x ** 3
# complete the lambda function

def fibonacci(n):
    # return a list of fibonacci numbers
    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))