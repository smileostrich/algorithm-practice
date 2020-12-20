import sys


N = int(sys.stdin.readline())
fi_li = [1, 1]

if N == 1:
    print(1)
elif N == 2:
    print(1)
else:
    for _ in range(N-2):
        fi_li.append(fi_li[-1] + fi_li[-2])
    print(fi_li[-1])