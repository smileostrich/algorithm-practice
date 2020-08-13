import sys

n = int(sys.stdin.readline())
r = -1
cycle = 0
while(r != n):
    if r == -1:
        if n < 10:
            r = int(str(n)+str(n))
            cycle += 1
            continue
        else:
            k = list(str(n))
            first = int(k[-1]) * 10
            second = int(list(str(int(k[0]) + int(k[1])))[-1])
            r = first + second
            cycle += 1
            continue
    else:
        if r < 10:
            r = int(str(r) + str(r))
            cycle += 1
            continue
        else:
            k = list(str(r))
            first = int(k[-1]) * 10
            second = int(list(str(int(k[0]) + int(k[1])))[-1])
            r = first + second
            cycle += 1
            continue

print(cycle)