T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li_mat = []
    cond = False
    for q in range(N):
        tmp = input()
        li_mat.append(tmp)
        for i in range(N-M+2):
            if cond == True:
                break
            for j in range(M // 2):
                if tmp[i + j] != tmp[i+M - j]:
                # if tmp[i + j] != tmp[N - 1 - j]:
                    break
            else:
                result = tmp[i:M+i]
                cond = True
    for k in range(N):
        if cond == True:
            break
        for i in range(N-M+2):
            for j in range(M // 2):
                if li_mat[i + j][k] != li_mat[i+M - j][k]:
                # if li_mat[i + j][k] != li_mat[N - 1 - j][k]:
                    break
            else:
                result = ''
                for p in range(M):
                    result += li_mat[i+p][k]
                cond = True

    print(f'#{tc} {result}')