def search(l, r, times, n):
    ans = -1
    while l <= r:
        mid = (l+r)//2
        cnt = 0
        for time in times:
            cnt += mid // time
        if cnt >= n:
            if ans == -1:
                ans = mid
            else:
                ans = min(ans, mid)
            r = mid -1
        else:
            l = mid + 1
    return ans


def solution(n, times):
    times.sort()
    left = 0
    right = times[-1]*n
    return search(left, right, times, n)


print(solution(6, [7, 10]))


# import heapq
#
# def solution(n, times):
#     hq = []
#     for i in times:
#         heapq.heappush(hq, (i,i))
#     cnt = 0
#     for i in range(n):
#         d1, d2 = heapq.heappop(hq)
#         heapq.heappush(hq, (d1+d2, d2))
#         cnt += d1-cnt
#     return cnt
#
# print(solution(6, [7, 10]))