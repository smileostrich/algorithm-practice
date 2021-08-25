li_dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
li_dp[0][0][0] = 1

for a in range(21):
    for b in range(21):
        for c in range(21):
            if a <= 0 or b <= 0 or c <= 0:
                li_dp[a][b][c] = 1
            elif a < b < c:
                li_dp[a][b][c] = li_dp[a][b][c-1] + li_dp[a][b-1][c-1] - li_dp[a][b-1][c]
            else:
                li_dp[a][b][c] = li_dp[a-1][b][c] + li_dp[a-1][b-1][c] + li_dp[a-1][b][c-1] - li_dp[a-1][b-1][c-1]

while True:
    a,b,c = map(int, input().split())
    if a==b==c==-1:
        break
    if a <= 0 or b <= 0 or c <= 0:
        result = li_dp[0][0][0]
    elif a > 20 or b > 20 or c > 20:
        result = li_dp[20][20][20]
    else:
        result = li_dp[a][b][c]
    print(f'w({a}, {b}, {c}) = {result}')