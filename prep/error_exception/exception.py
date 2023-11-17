if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        try:
            a, b = map(int, input().split())
            result = a // b
            print(result)
        except (ZeroDivisionError, ValueError) as e:
            print(f"Error Code: {e}")
