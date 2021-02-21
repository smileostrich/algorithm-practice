T = int(input())
for tc in range(1, T+1):
    N = int(input())
    size = N * N
    mat = [[0]*N for _ in range(N)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    cnt = 0
    dir = 0
    x = 0
    y = 0
    while cnt < size:
        if 0 <= x <= N-1 and 0 <= y <= N-1 and mat[y][x] == 0:
            cnt += 1
            mat[y][x] = cnt
        else:
            x -= dx[dir]
            y -= dy[dir]
            dir = (dir + 1)%4
        x += dx[dir]
        y += dy[dir]
    print(f'#{tc}')
    for i in mat:
        print(*i)