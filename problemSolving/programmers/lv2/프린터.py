from collections import deque

def solution(priorities, location):
    importance = priorities
    li_wait = deque(zip(range(len(priorities)),priorities))
    importance.sort()
    cnt = 1
    while li_wait:
        cur = li_wait.popleft()
        imp = importance.pop()
        if cur[1] != imp:
            li_wait.append(cur)
            importance.append(imp)
        else:
            if cur[0] == location:
                return cnt
            else:
                cnt += 1





print(solution([2, 1, 3, 2], 2))