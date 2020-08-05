# 10분

import sys

n = int(sys.stdin.readline())
list = []
k = [list.append(int(sys.stdin.readline())) for _ in range(n)]
list.sort()
for i in range(len(list)):
    print(list[i])
