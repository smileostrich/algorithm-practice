import sys

n2 = [2, 4, 8, 6]
n3 = [3, 9, 7, 1]
n4 = [4, 6]
n7 = [7, 9, 3, 1]
n8 = [8, 4, 2, 6]
n9 = [9, 1]

n = int(sys.stdin.readline())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    a %= 10

    if a == 0:
        print(10)
        continue
    elif a == 1:
        print(1)
        continue
    elif a == 2:
        print(n2[(b - 1) % 4])
    elif a == 3:
        print(n3[(b - 1) % 4])
    elif a == 4:
        print(n4[(b - 1) % 2])
    elif a == 5:
        print(5)
        continue
    elif a == 6:
        print(6)
        continue
    elif a == 7:
        print(n7[(b - 1) % 4])
        continue
    elif a == 8:
        print(n8[(b - 1) % 4])
        continue
    elif a == 9:
        print(n9[(b - 1) % 2])
        continue

