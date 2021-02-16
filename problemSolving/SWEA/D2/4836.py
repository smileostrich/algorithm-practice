T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li_red = []
    li_blue = []
    li_mat = [[0]*10 for _ in range(10)]
    cnt = 0
    for _ in range(N):
        tmp = list(map(int, input().split()))
        li_tmp, type = tmp[:-1], tmp[-1]
        if type == 1:
            li_red.append(li_tmp)
        else:
            li_blue.append(li_tmp)
    for i in li_red:
        tmp_x = i[2] - i[0] + 1
        tmp_y = i[3] - i[1] + 1
        for a in range(tmp_x):
            for b in range(tmp_y):
                li_mat[i[1]+b][i[0] + a] = 1
    for j in li_blue:
        tmp_x = j[2] - j[0] + 1
        tmp_y = j[3] - j[1] + 1
        for a in range(tmp_x):
            for b in range(tmp_y):
                if li_mat[j[1] + b][j[0] + a] == 1:
                    cnt += 1
    print(f'#{tc} {cnt}')