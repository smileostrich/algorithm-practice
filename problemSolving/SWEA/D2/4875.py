dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(x,y):
    visited[y][x] = 1
    for cur in range(4):
        new_x, new_y = x+dx[cur], y+dy[cur]
        if 0<=new_x<N and 0<=new_y<N and not visited[new_y][new_x]:
            if matrix[new_y][new_x] == 3:
                return 1
            elif matrix[new_y][new_x] == 0:
                if dfs(new_x, new_y):
                    return 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                sx,sy = j,i
                break
    if dfs(sx,sy):
        result = 1
    else:
        result = 0
    print(f'#{tc} {result}')