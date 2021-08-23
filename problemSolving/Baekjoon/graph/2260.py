from collections import deque

def bfs():
    queue = deque([[0,0,1]])
    while queue:
        x, y, w = queue.popleft()
        if y == N - 1 and x == M - 1:
            return li_visited[y][x][w]
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N:
                if li_matrix[ny][nx] == 1 and w == 1:
                    li_visited[ny][nx][0] = li_visited[y][x][1] + 1
                    queue.append([nx, ny, 0])
                elif li_matrix[ny][nx] == 0 and li_visited[ny][nx][w] == 0:
                    li_visited[ny][nx][w] = li_visited[y][x][w] + 1
                    queue.append([nx, ny, w])
    return -1


N, M = map(int, input().split())
li_matrix = []
for i in range(N):
    li_matrix.append(list(map(int, list(input()))))
dir = [(1,0),(-1,0),(0,-1),(0,1)]
li_visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
li_visited[0][0][1] = 1
print(bfs())