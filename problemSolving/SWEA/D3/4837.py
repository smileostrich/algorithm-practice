# 풀이1
from itertools import combinations

T = int(input())
rang = [i for i in range(1,12+1)]
for tc in range(1, T+1):
    N, K = map(int, input().split())
    result = []
    cnt = 0
    test = combinations(rang, N)
    for i in test:
        if sum(i) == K:
           cnt += 1
    print(f'#{tc} {cnt}')

# 풀이 2
