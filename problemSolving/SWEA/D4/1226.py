from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    dq = deque([(x,y)])
    while dq:
        cx,cy = dq.popleft()
        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            if 0<=nx<16 and 0<=ny<16 and li_matrix[ny][nx] != 1 and visited[ny][nx] == 0:
                if li_matrix[ny][nx] == 3:
                    return 1
                else:
                    visited[ny][nx] += visited[cy][cx] + 1
                    dq.append((nx,ny))
    else:
        return 0


for _ in range(10):
    tc = int(input())
    li_matrix = []
    visited = [[0]*16 for _ in range(16)]
    for i in range(16):
        tmp = list(map(int, list(input())))
        li_matrix.append(tmp)
        for j in range(16):
            if tmp[j] == 2:
                sx, sy = j, i
    print(f'#{tc} {bfs(sx,sy)}')