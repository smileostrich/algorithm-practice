N = int(input())
li_matrix = [list(map(int, input().split())) for i in range(N)]
li_visited = [0 for _ in range(N)]
ans = int(1e9)

def dfs(idx, cnt):
    global ans
    if cnt == N // 2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if i != j:
                    if li_visited[i] and li_visited[j]:
                        start += li_matrix[i][j]
                    elif not li_visited[i] and not li_visited[j]:
                        link += li_matrix[i][j]
        ans = min(ans, abs(start - link))
    for i in range(idx, N):
        if li_visited[i]:
            continue
        li_visited[i] = 1
        dfs(i+1, cnt+1)
        li_visited[i] = 0

dfs(0,0)
print(ans)
