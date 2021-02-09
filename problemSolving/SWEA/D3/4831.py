T = int(input())
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    mli = list(map(int, input().split()))
    cur = 0
    ch = K
    cnt = 0
    for i in range(1, N):
        ch -= 1
        if ch < 0:
            cnt = 0
            break
        if mli[cur] == i:
            if cur == M-1:
                if N-i > ch:
                    ch = K
                    cnt += 1
            elif ch-(mli[cur+1] - mli[cur]) < 0:
                cur += 1
                cnt += 1
                ch = K
            else:
                cur += 1
        elif mli[cur] < i and cur < M-1:
            cur += 1
    print(f'#{test_case} {cnt}')