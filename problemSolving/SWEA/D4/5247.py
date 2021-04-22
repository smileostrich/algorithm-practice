from collections import deque

def recur(cur):
    dq = deque([(cur,0)])
    visited[cur] = True
    while dq:
        cur, cnt = dq.popleft()
        if cur == M:
            return cnt
        else:
            if 0<cur+1 <= 1000000 and cur+1 not in visited:
                dq.append((cur+1, cnt+1))
                visited[cur+1] = True
            if 0< cur-1 <= 1000000 and cur-1 not in visited:
                dq.append((cur-1, cnt+1))
                visited[cur-1] = True
            if 0<cur*2 <= 1000000 and cur*2 not in visited:
                dq.append((cur*2, cnt+1))
                visited[cur*2] = True
            if 0< cur-10<=1000000 and cur-10 not in visited:
                dq.append((cur-10, cnt+1))
                visited[cur-10] = True

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = {}
    print(f'#{tc} {recur(N)}')