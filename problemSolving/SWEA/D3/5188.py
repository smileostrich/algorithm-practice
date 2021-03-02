import math


def dfs(x,y):
    global sub_result, result
    if result < sub_result:
        return
    if y == N-1 and x == N-1:
        result = sub_result
        return
    for dir in range(2):
        new_x = x + dx[dir]
        new_y = y + dy[dir]
        if 0<=new_y<N and 0<=new_x<N and (new_x, new_y) not in visited:
            visited.append((new_x, new_y))
            sub_result += matrix[new_y][new_x]
            dfs(new_x, new_y)
            visited.remove((new_x,new_y))
            sub_result -= matrix[new_y][new_x]

# T = 1
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = []
    dx = [1,0]
    dy = [0,1]

    sub_result = matrix[0][0]
    result = math.inf
    dfs(0,0)
    print(f'#{tc} {result}')