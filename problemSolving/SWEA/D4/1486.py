def dfs(idx, height):
    global min_height
    if B <= height < min_height:
        min_height = height
    if idx == N:
        return
    dfs(idx + 1, height)
    dfs(idx + 1, height + li_height[idx])

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    li_height = list(map(int, input().split()))
    min_height = 200000
    dfs(0, 0)
    print(f'#{tc} {min_height-B}')