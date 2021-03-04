from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    dq_n = deque(map(int, input().split()))
    for _ in range(M):
        dq_n.append(dq_n.popleft())
    print(f'#{tc} {dq_n[0]}')