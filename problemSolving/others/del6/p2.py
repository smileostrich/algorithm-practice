def problem(n, k):
  dp = [[[-1] * (k+1) for _ in range(n+1)] for __ in range(n+1)]
  return solution(n, n, k, dp)

def solution(r, c, k, dp):
  if dp[r][c][k] == -1:
    if r < k or c < k:
      dp[r][c][k] = 0
    elif k == 0:
      dp[r][c][k] = 1
    else:
      dp[r][c][k] = solution(r-1, c-1, k-1, dp) * c + solution(r-1, c, k, dp)

  return dp[r][c][k]

# def problem(n, k):
#   return solution(n, n, k)
#
# def solution(r, c, k):
#     if r < k or c < k:
#       return 0
#     elif k == 0:
#       return 1
#     else:
#       return solution(r-1, c-1, k-1) * c + solution(r-1, c, k)

print(problem(8,6))