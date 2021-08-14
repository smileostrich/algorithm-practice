N, K = map(int, input().split())
li_dp = [[[False for _ in range(3)] for _ in range(4)] for _ in range(N+1)]
li_date = [False for _ in range(N+1)]

def setDP(day):
    for i in range(1,4):
        if li_date[day] and i != li_date[day]:
            continue
        for j in range(1,4):
            if i == j:
                li_dp[day][i][2] = li_dp[day-1][j][1]
            else:
                li_dp[day][i][1] += li_dp[day-1][j][1] + li_dp[day-1][j][2]
                li_dp[day][i][1] %= 10000

for i in range(N):
   t1,t2 = map(int, input().split())
   li_date[t1] = t2
if li_date[1]:
    li_dp[1][li_date[1]][1] = 1
else:
    li_dp[1][1][1] = 1
    li_dp[1][2][1] = 1
    li_dp[1][3][1] = 1

for i in range(2, N+1):
    setDP(i)

print((li_dp[N][1][1] + li_dp[N][1][2] + li_dp[N][2][1]+ li_dp[N][2][2] + li_dp[N][3][1] + li_dp[N][3][2]) % 10000)