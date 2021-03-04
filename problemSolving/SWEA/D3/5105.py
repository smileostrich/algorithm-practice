from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    global cnt
    dq = deque([(x,y)])
    while dq:
        cx, cy = dq.popleft()
        for i in range(4):
            nx,ny = cx + dx[i], cy + dy[i]
            if 0<=nx<N and 0<=ny<N and matrix[ny][nx] != 1 and visited[ny][nx] == 0:
                if matrix[ny][nx] == 3:
                    return visited[cy][cx]
                else:
                    dq.append((nx,ny))
                    visited[ny][nx] = visited[cy][cx] + 1
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                sx,sy = j, i
                break
    print(f'#{tc} {bfs(sx, sy)}')