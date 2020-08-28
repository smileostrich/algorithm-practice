# 다시풀어보기
import sys


T = int(sys.stdin.readline().rstrip())
near = ((0, 1), (0, -1), (1, 0), (-1, 0))


def bfs(x,y):
    queue = [(x,y)]
    mat[x][y] = 0
    while queue:
        x, y = queue.pop(0)

        for di, dj in near:
            newX, newY = x+di, y+dj
            if not (0 <= newX < m and 0 <= newY < n):
                continue
            if mat[newX][newY] == 1:
                queue.append((newX, newY))
                mat[newX][newY] = 0
    return 1


for t in range(T):
    n, m, k = map(int, sys.stdin.readline().split())

    mat = [[0] * n for _ in range(m)]
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        mat[b][a] = 1
    cnt = 0
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                cnt += bfs(i, j)

    print(cnt)