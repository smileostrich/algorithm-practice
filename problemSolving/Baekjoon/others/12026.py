import math

N = int(input())
boj = input()

memo = [math.inf] * N
memo[0] = 0

def get_last(cur):
    if cur == 'B':
        return 'J'
    elif cur == 'O':
        return 'B'
    else:
        return 'O'

for i in range(1, N):
    prev = get_last(boj[i])
    for j in range(i):
        if boj[j] == prev:
            memo[i] = min(memo[i], memo[j]+(i-j)*(i-j))
if memo[-1] == math.inf:
    print(-1)
else:
    print(memo[-1])