# 35분

from sys import stdin
import heapq

inp = lambda: stdin.readline().rstrip()


N = int(inp())
# li_meeting = [tuple(map(inp().split())) for _ in range(N)]
hq_meeting = []
for _ in range(N):
    s, e = map(int, inp().split())
    heapq.heappush(hq_meeting, (e, s))

cur_e, s = heapq.heappop(hq_meeting)
ans = 1

while hq_meeting:
    # e, s = hq_meeting[0]
    e,s = heapq.heappop(hq_meeting)
    if cur_e > s:
        # heapq.heappop(hq_meeting)
        continue
    else:
        cur_e = e
        ans += 1
        continue
        # heapq.heappop(hq_meeting)
print(ans)


# start_time
# end_time