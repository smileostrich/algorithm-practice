from collections import deque
from collections import defaultdict

def solution(jobs):
    d_jobs = deque(jobs)
    time = jobs[0][0]
    result = []
    last = -1
    while d_jobs:
        li_tmp = []
        while d_jobs:
            cur = d_jobs.popleft()
            if cur[0] > time:
                d_jobs.appendleft(cur)
                break
            else:
                li_tmp.append(cur)
        if len(li_tmp) == 1:
            time += li_tmp[0][1]
            if len(result) == 0:
                result.append(li_tmp[0][2])
            else:
                if result[-1] != li_tmp[0][2]:
                    result.append(li_tmp[0][2])
            last = li_tmp[0][2]
        elif last == -1:
            dic_cnt = defaultdict(int)
            dic_group = defaultdict(list)
            for i in li_tmp:
                dic_cnt[i[2]] += i[3]
                dic_group[i[2]].append(i)
            highest = max(dic_cnt.values())
            li_high = []
            for k,v in dic_cnt.items():
                if v == highest:
                    li_high.append(k)
            li_high.sort()
            last = li_high[0]
            for i in dic_group.pop(li_high[0]):
                time += i[1]
                if len(result) == 0:
                    result.append(i[2])
                else:
                    if result[-1] != i[2]:
                        result.append(i[2])
            for i in dic_group.values():
                d_jobs.extendleft(i)
        else:
            last_idx = 0
            while li_tmp and last_idx < len(li_tmp):
                if li_tmp[last_idx][2] == last:
                    time += li_tmp.pop(last_idx)[1]
                else:
                    last_idx += 1
            d_jobs.extendleft(li_tmp)
    return result



print(solution(	[[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]]))