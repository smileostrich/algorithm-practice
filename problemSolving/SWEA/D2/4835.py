T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    h_li = 0
    s_li = 0
    for p in range(M):
        h_li += li[p]
        s_li += li[p]
    for i in range(1, N-M+1, 1):
        t_sum = 0
        for p in range(M):
            t_sum += li[i+p]
        if t_sum > h_li:
            h_li = t_sum
        elif t_sum < s_li:
            s_li = t_sum
    print(f'#{test_case} {h_li-s_li}')