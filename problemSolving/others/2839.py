import sys

N = int(sys.stdin.readline())
li = [-1] * (N+1)

for i in range(3, N+1):
    if i == 3:
        li[3] = 1
    elif i == 5:
        li[5] = 1
    elif li[i-3] != -1 and li[i-5] != -1:
        li[i] = min(li[i-3]+1, li[i-5]+1)
    elif li[i - 3] != -1:
        li[i] = li[i - 3] + 1
    elif li[i-5] != -1:
        li[i] = li[i-5]+1
        # elif li[i-3] == -1 and li[i-5] == -1:
        #     li[i] = -1

print(li[N])