import sys


N = int(input())
li_n = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
li_dp = [[0 for _ in range(i)] for i in range(1,N+1)]
li_dp[0][0] = li_n[0][0]
for i in range(0,N-1):
    for j in range(len(li_n[i])):
        li_dp[i+1][j] = max(li_dp[i+1][j], li_n[i+1][j]+li_dp[i][j])
        li_dp[i+1][j+1] = max(li_dp[i+1][j+1], li_n[i+1][j+1]+li_dp[i][j])
print(max(li_dp[N-1]))