from collections import namedtuple

N, columns = int(input()), input().split()
Student = namedtuple('Student', columns)
print("{:.2f}".format(sum([int(Student(*input().split()).MARKS) for _ in range(N)]) / N))
