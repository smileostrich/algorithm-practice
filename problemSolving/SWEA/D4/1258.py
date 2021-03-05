def search_size(x,y):
    y_cnt = 0
    x_cnt = 0
    for i in range(y, N):
        if matrix[i][x] != 0:
            y_cnt += 1
        else:
            break
    for i in range(x, N):
        if matrix[y][i] != 0:
            x_cnt += 1
        else:
            break
    ans.append([y_cnt, x_cnt, y_cnt*x_cnt])
    init(x,y,x_cnt,y_cnt)

def init(x,y, x_cnt, y_cnt):
    for i in range(y, y+y_cnt):
        for j in range(x, x+x_cnt):
            matrix[i][j] = 0

def counting_sort(idx):
    cnt = [0] * 10001
    sort_ans = [0] * len(ans)
    for i in range(len(ans)):
        cnt[ans[i][idx]] += 1
    for i in range(1, len(cnt)):
        cnt[i] += cnt[i-1]
    for i in range(len(ans)-1,-1,-1):
        sort_ans[cnt[ans[i][idx]]-1] = ans[i]
        cnt[ans[i][idx]] -= 1
    return sort_ans


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    ans = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0:
                search_size(j,i)
    ans = counting_sort(0)
    ans = counting_sort(2)
    print(f'#{tc} {len(ans)}', end=' ')
    for i in range(len(ans)):
        print(f'{ans[i][0]} {ans[i][1]}', end=' ')
    print()