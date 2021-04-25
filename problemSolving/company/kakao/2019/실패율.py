import heapq
from collections import Counter

def solution(N, stages):
    hq = []
    li_cnt = [0 for _ in range(502)]
    dic_cnt = Counter(stages)
    for st in stages:
        if st >= N:
            st = N
        for i in range(1, st+1):
            li_cnt[i] += 1
    for i in range(1,N+1):
        if li_cnt[i] == 0:
            li_cnt[i] = 1
        heapq.heappush(hq, (-1*dic_cnt.get(i,0)/li_cnt[i],i))
    result = []
    for _ in range(len(hq)):
        result.append(heapq.heappop(hq)[1])
    return result

print(solution(	5, [2, 1, 2, 6, 2, 4, 3, 3]))