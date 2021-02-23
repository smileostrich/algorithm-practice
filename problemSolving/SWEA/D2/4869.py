T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x = N
    new_x = x // 10
    if new_x <= 2:
        memo = [0,1,3]
    else:
        memo = [0] * (new_x+1)
        memo[1] = 1
        memo[2] = 3
        for i in range(3,new_x+1):
            memo[i] = memo[i-1] + memo[i-2]*2
    print(f'#{tc} {memo[new_x]}')