from collections import deque


lf = [(0,-1),(-1,0)]
rf = [(0,1),(1,0)]


def bfs(x,y):
    dq = deque([(x,y)])
    while dq:
        cx,cy = dq.popleft()
        for dx,dy in lf:
            nx, ny = cx+dx, cy+dy
            if 0<=nx<N and 0<=ny<N and not visited[ny][nx] == 0 and :


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    bfs(x,y)
