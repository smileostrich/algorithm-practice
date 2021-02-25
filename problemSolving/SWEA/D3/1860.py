# T = 1
T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int, input().split())
    sec = list(map(int, input().split()))
    # N, M, K = 2,2,1
    # sec = [4,2]
    sec.sort()
    for i in range(N):
        if sec[i] // M * K - i < 1:
            print(f'#{tc} Impossible')
            break
    else:
        print(f'#{tc} Possible')