def back(idx, cnt, li_visited):
    global low
    if low > cnt:
        if idx == N:
            if low > cnt:
                low = cnt
            return
        else:
            for k, val in enumerate(li_visited):
                if not val:
                    li_visited[k] = True
                    back(idx+1, cnt+li_factory[idx][k], li_visited)
                    li_visited[k] = False

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    li_factory = [list(map(int, input().split())) for _ in range(N)]
    low = 100 * N
    back(0,0,[False]*N)

    print(f'#{tc} {low}')