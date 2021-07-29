def solution(grid):
    x, y = len(grid[0]), len(grid)
    dp = [[0 for _ in range(x)] for _ in range(y)]

    for i in range(y):
        for j in range(x):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
            else:
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
                elif i > 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
    return dp[y-1][x-1]

print(solution([[1, 8, 3, 2], [7, 4, 6, 5] ]))