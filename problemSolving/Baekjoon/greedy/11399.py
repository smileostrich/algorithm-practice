# 두번째 풀이 greedy
N = int(input())
li_time = list(map(int, input().split()))
li_time.sort()
ans = 0
s = 0
for i in li_time:
    s += i
    ans += s
print(ans)

# 첫번째
# 10분

# from sys import stdin
# import heapq
#
#
# inp = lambda: stdin.readline().rstrip()
#
# N = int(inp())
# li_draw = list(map(int, inp().split()))
# heapq.heapify(li_draw)
# li_sum = []
#
# for _ in range(N):
#     if li_sum:
#         li_sum.append(li_sum[-1] + heapq.heappop(li_draw))
#     else:
#         li_sum.append(heapq.heappop(li_draw))
#
# print(sum(li_sum))