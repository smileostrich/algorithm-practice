def dfs(r, c, d):
    global cnt, start
    stack = [(r, c, d)]
    while stack:
        cr, cc, cd = stack.pop()
        if cd > cnt:
            cnt = cd
            start = li_matrix[r][c]
        elif cd == cnt and start > li_matrix[r][c]:
            start = li_matrix[r][c]
        for dr, dc in delta:
            nr = dr + cr
            nc = dc + cc
            if 0 <= nr < N and 0 <= nc < N and li_matrix[nr][nc] == li_matrix[cr][cc] + 1:
                stack.append((nr, nc, cd + 1))

T = int(input())
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for tc in range(1, T + 1):
    N = int(input())
    li_matrix = [list(map(int, input().split())) for x in range(N)]
    cnt = 0
    start = -1
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            visited[i][j] = 1
            dfs(i, j, 1)
    print(f'#{tc} {start} {cnt}')