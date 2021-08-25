N = int(input())
li_n = list(map(int, input().split()))
li_dp = [0]*N
li_dp[0] = li_n[0]
for i in range(1, len(li_n)):
    li_dp[i] = max(li_dp[i-1]+li_n[i],li_n[i])
print(max(li_dp))