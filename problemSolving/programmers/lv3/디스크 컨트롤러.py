import heapq

def solution(jobs):
    li_hq = []
    for i,v in jobs:
        heapq.heappush(li_hq, (v,i))
    cur = 0
    li_answer = []
    while li_hq:
        time, come = heapq.heappop(li_hq)
        wait = cur-come
        li_answer.append(time+wait)
        cur += time
    cur = 0
    heapq.heapify(jobs)
    li_answer2 = []
    while jobs:
        come, time = heapq.heappop(jobs)
        wait = cur - come
        li_answer2.append(time + wait)
        cur += time
    return min(sum(li_answer)//len(li_answer), sum(li_answer2)//len(li_answer2))


print(solution(	[[0, 3], [1, 9], [2, 6]]))