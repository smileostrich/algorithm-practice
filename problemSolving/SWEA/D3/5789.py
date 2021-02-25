T = int(input())
# T = 1
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    li_box = [0 for _ in range(N+1)]
    for i in range(1,Q+1):
        l, r = map(int, input().split())
        for j in range(l,r+1):
            li_box[j] = i
    print(f'#{tc}',*(li_box[1:]))