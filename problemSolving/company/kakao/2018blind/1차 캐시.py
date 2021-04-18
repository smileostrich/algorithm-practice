from collections import deque

def solution(cacheSize, cities):
    dq_cache = deque([])
    dic_cache = {i.lower():False for i in cities}
    time = 0
    if cacheSize == 0:
        return len(cities) * 5
    for cur in cities:
        cur = cur.lower()
        if len(dq_cache) < cacheSize:
            if dic_cache[cur]:
                dq_cache.remove(cur)
                dq_cache.appendleft(cur)
                time += 1
            else:
                dic_cache[cur] = True
                dq_cache.appendleft(cur)
                time += 5
        else:
            if dic_cache[cur]:
                dq_cache.remove(cur)
                dq_cache.appendleft(cur)
                time += 1
            else:
                out = dq_cache.pop()
                dic_cache[out] = False
                dic_cache[cur] = True
                dq_cache.appendleft(cur)
                time += 5
    return time


print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))