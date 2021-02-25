T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    li_pr = list(map(int, input().split()))
    result = 0
    max_val = 0
    for i in range(N-1,-1,-1):
        if li_pr[i] > max_val:
            max_val = li_pr[i]
        else:
            result += max_val - li_pr[i]
    print(f'#{tc} {result}')
