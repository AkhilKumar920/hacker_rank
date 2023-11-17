import calendar

if __name__ == '__main__':
    month, day, year = map(int, input().split())
    day_of_week = calendar.weekday(year, month, day)
    print(calendar.day_name[day_of_week].upper())
