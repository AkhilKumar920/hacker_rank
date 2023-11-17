from datetime import datetime, timedelta

def time_delta(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    time_format = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, time_format)
    t2 = datetime.strptime(t2, time_format)
    delta = abs(int((t1 - t2).total_seconds()))
    return str(delta)

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        t1 = input()
        t2 = input()
        result = time_delta(t1, t2)
        print(result)
