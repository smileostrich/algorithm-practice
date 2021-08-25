N = int(input())
li_n = [list(map(int, input().split())) for _ in range(N)]
li_n.sort(key=lambda x:x[0])
li_dp = [1]*N
for i in range(N):
    for j in range(i):
        if li_n[i][1] > li_n[j][1]:
            li_dp[i] = max(li_dp[i], li_dp[j]+1)
print(N-max(li_dp))