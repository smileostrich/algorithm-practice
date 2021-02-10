T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int, input().split())
    li_a = list(map(int, input().split()))
    li_b = list(map(int, input().split()))
    high = 0
    if N > M:
        li_a, li_b = li_b, li_a
        N, M = M, N
    for i in range(0, M-N+1):
        s_tmp = 0
        for j in range(N):
            s_tmp += li_b[j+i]*li_a[j]
        if s_tmp > high:
            high = s_tmp
    print(f'#{test_case} {high}')