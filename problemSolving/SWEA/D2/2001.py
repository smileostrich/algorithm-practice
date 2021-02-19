T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li_matrix = [list(map(int, input().split())) for _ in range(N)]
    highst = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            tmp_sum = 0
            for k in range(M):
                for p in range(M):
                    tmp_sum += li_matrix[i+k][j+p]
            if highst < tmp_sum:
                highst = tmp_sum

    print(f'#{tc} {highst}')