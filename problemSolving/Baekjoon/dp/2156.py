N = int(input())
li_wine = [int(input()) for _ in range(N)]
li_dp = [0 for _ in range(N)]
li_dp[0] = li_wine[0]
if N >= 2:
    li_dp[1] = li_wine[1]+li_dp[0]
if N >= 3:
    li_dp[2] = max(li_dp[0]+li_wine[2], li_wine[1]+li_wine[2], li_dp[1])
for i in range(3, N):
    li_dp[i] = max(li_dp[i-2]+li_wine[i], li_dp[i-3]+li_wine[i-1]+li_wine[i], li_dp[i-1])
print(li_dp[N-1])