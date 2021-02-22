T = int(input())
# T = 1
for tc in range(1, T+1):
    N = int(input())
    li_mat = [list(map(int, input().split())) for _ in range(N)]
    # N = 3
    # li_mat = [[1,2,3],[4,5,6],[7,8,9]]
    li_90 = list(zip(*li_mat[::-1]))
    li_180 = list(zip(*li_90[::-1]))
    li_270 = list(zip(*li_180[::-1]))
    new_90 = []
    new_180 = []
    new_270 = []
    for i in li_90:
        new_90.append(''.join(map(str,i)))
    for i in li_180:
        new_180.append(''.join(map(str,i)))
    for i in li_270:
        new_270.append(''.join(map(str, i)))
    li_result = []
    for i in range(N):
        li_tmp = []
        li_tmp.append(new_90[i])
        li_tmp.append(new_180[i])
        li_tmp.append(new_270[i])
        li_result.append(li_tmp)
    print(f'#{tc}')
    for i in li_result:
        print(f'{" ".join(i)}')