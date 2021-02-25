T = 1
# T = int(input())
for tc in range(1,T+1):
    # N, M, K = map(int, input().split())
    # sec = list(map(int, input().split()))
    N, M, K = 2,2,1
    sec = [4,2]
    sec.sort()
    mx = sec[-1]
    cnt = 0

    fk = [0]*(max(mx, M)+1)
    for i in range(0,len(fk),M):
        for j in range(i-1):
            fk[i] += K
            for p in range(1,M):
                if i+p < len(fk):
                    fk[i+p] += K
    result = ''
    for i in sec:
        if fk[i] == 0:
            result = "Impossible"
            break
        else:
            for j in range(i, len(fk)):
                fk[j] -= 1
    else:
        result = "Possible"
    print(f'#{tc} {result}')
