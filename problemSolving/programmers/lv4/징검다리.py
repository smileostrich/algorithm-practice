def solution(distance, rocks, n):
    answer = 0
    sorted_rocks = sorted(rocks)
    sorted_rocks.append(distance)
    left = 0
    right = distance
    while (left <= right):
        mid = (left + right) // 2
        cnt = 0
        p = 0
        for i in range(len(sorted_rocks)):
            if sorted_rocks[i] - p < mid:
                cnt += 1
            else:
                p = sorted_rocks[i]
        if cnt > n:
            right = mid - 1
        else:
            left = mid + 1
            answer = mid
    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))

# from itertools import combinations
#
#
# def solution(distance, rocks, n):
#     rocks.sort()
#     li_idx = list(combinations(range(len(rocks)), len(rocks)-n))
#     rocks.append(distance)
#     high = 0
#     for idxs in li_idx:
#         for idx, i in enumerate(idxs):
#             if idx == 0:
#                 tmp_low = rocks[i]
#             else:
#                 if rocks[i]-rocks[idxs[idx-1]] < tmp_low:
#                     tmp_low = rocks[i] - rocks[idxs[idx-1]]
#         if rocks[-1] - rocks[idxs[-1]] < tmp_low:
#             tmp_low = rocks[-1] - rocks[idxs[-1]]
#         if high < tmp_low:
#             high = tmp_low
#     return high
#
#
# print(solution(25, [2, 14, 11, 21, 17], 2))