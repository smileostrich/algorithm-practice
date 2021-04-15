def dfs(cur):
    global tmp_sum, low

    if tmp_sum < low:
        visited[cur] = True
        if False not in visited:
            tmp_sum += li_matrix[cur][0]
            if tmp_sum < low:
                low = tmp_sum
            tmp_sum -= li_matrix[cur][0]
        else:
            for neighbor in range(N):
                if visited[neighbor] == False:
                    tmp_sum += li_matrix[cur][neighbor]
                    dfs(neighbor)
                    tmp_sum -= li_matrix[cur][neighbor]
        visited[cur] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li_matrix = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    tmp_sum = 0
    low = 10000
    dfs(0)
    print(f'#{tc} {low}')
