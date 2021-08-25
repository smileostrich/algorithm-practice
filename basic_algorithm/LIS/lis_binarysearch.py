# way1
# def lis(arr):
#     if not arr:
#         return 0
#
#     INF = float('inf')
#     d = [INF] * (len(arr)+1)
#     d[0] = -INF
#     d[1] = arr[0]
#     answer = 1
#
#     def search(lo, hi, n):
#         if lo == hi:
#             return lo
#         elif lo + 1 == hi:
#             return lo if d[lo] >= n else hi
#
#         mid = (lo + hi) // 2
#         if d[mid] == n:
#             return mid
#         elif d[mid] < n:
#             return search(mid+1, hi, n)
#         else:
#             return search(lo, mid, n)
#
#
#     for n in arr:
#         if d[answer] < n:
#             answer += 1
#             d[answer] = n
#         else:
#             next_loc = search(0, answer, n)
#             d[next_loc] = n
#
#     return answer

# way2 비용 길이
def solution(limit, arr):
    size = len(arr)
    d = [[0 for _ in range(2)] for _ in range(size)]
    if arr[0] <= limit:
        d[0][0] = 1 # 길이
        d[0][1] = arr[0] # 비용
    answer = d[0][0]
    for i in range(1, size):
        if arr[i] + d[i-1][1] <= limit:
            d[i][0] = d[i-1][0] + 1
            d[i][1] = d[i-1][1] + arr[i]
        else:
            if arr[i] <= limit:
                d[i][0] = 1
                d[i][1] = arr[i]
        if answer < d[i][0]:
            answer = d[i][0]
    return answer

print(solution(5,[1,2,3,4,5]))

# way 3 n**2
# N = int(input())
# A = list(map(int, input().split()))
#
# dp = [1] * N
#
# for i in range(N):
#     for j in range(i):
#         if A[j] < A[i]:
#             dp[i] = max(dp[i],dp[j]+1)
#
# print(max(dp))

# way 4 bisect 모듈 사용
#이진탐색 코드, 같은 수일 경우 왼쪽 index를 돌려준다

# from bisect import bisect_left
#
# N = int(input())
# li_n = list(map(int, input().split()))
#
# li_dp = [li_n[0]]
# for idx in range(1,N):
#     if li_n[idx] > li_dp[-1]:
#         li_dp.append(li_n[idx])
#     else:
#         insert_idx = bisect_left(li_dp, li_n[idx])
#         li_dp[insert_idx] = li_n[idx]
# print(len(li_dp))