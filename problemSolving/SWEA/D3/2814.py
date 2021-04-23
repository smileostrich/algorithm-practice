def dfs(e, cnt):
    global high
    visited[e] = 1
    if high < cnt:
        high = cnt
    for i in range(1, N+1):
        if adjList[e][i] and not visited[i]:
            dfs(i,cnt+1)
    visited[e] = 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adjList = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        x,y = map(int, input().split())
        adjList[x][y] = 1
        adjList[y][x] = 1
    visited = [0] * (N+1)
    high = 0
    for i in range(1,N+1):
        dfs(i,1)
    print(f'#{tc} {high}')