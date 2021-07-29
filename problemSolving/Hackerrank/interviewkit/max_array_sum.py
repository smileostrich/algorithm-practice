def maxSubsetSum(arr):
    if len(arr) == 1:
        if arr[0] > 0:
            return arr[0]
        else:
            return 0
    dp = [arr[0], max(arr[:2])] + [0] * (len(arr) - 2)
    for i in range(2, len(arr)):
        dp[i] = max(dp[i-2]+arr[i], arr[i], dp[i-1])
    return dp[-1]


print(maxSubsetSum([-11,-2]))