N = int(input())
li_dp = [0]*(1000001)
li_dp[1] = 1
li_dp[2] = 2

for i in range(3,N+1):
    li_dp[i] = (li_dp[i-2]+li_dp[i-1])%15746
print(li_dp[N])