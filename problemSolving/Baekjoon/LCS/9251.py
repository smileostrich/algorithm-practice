a = input()
b = input()
li_dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
for i in range(1,len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            li_dp[i][j] = li_dp[i-1][j-1] + 1
        else:
            li_dp[i][j] = max(li_dp[i-1][j], li_dp[i][j-1])
print(li_dp[-1][-1])