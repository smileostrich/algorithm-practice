import heapq

def solution(genres, plays):
    dic_re = dict()
    for idx, val in enumerate(genres):
        if dic_re.get(val):
            heapq.heappush(dic_re[val], (-plays[idx], idx, plays[idx]))
        else:
            dic_re[val] = [(-plays[idx], idx, plays[idx])]

    hq_cnt = []
    for i,v in dic_re.items():
        heapq.heappush(hq_cnt, (-sum(list(zip(*v))[2]), i))
    result = []
    while hq_cnt:
        v, i = heapq.heappop(hq_cnt)
        t_cnt = 0
        while t_cnt < 2 and dic_re[i]:
            result.append(heapq.heappop(dic_re[i])[1])
            t_cnt += 1
    return result





print(solution(	["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))