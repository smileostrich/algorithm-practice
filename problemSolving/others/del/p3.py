from collections import deque

# def dfs():
#     if

def solution(K, A):
    for target in range(1, 1000000):
        q = deque([(0,p,A.copy()) for p in set(A)])
        while q:
            cnt, lane, li_tmp = q.popleft()
            cnt += 1
            while lane <= K:
                for tmp in li_tmp:
                    if tmp == lane:
                        li_tmp.pop(tmp)
                        lane += 1
                        break
            if cnt == target:
                if not li_tmp:
                    return target
            else:
                for p in set(A):
                    if p !=
                    q.append()


print(solution(5, [1, 3, 4, 2, 5]))