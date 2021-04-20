import heapq,math


def solution(operations):
    hq = []
    high = -math.inf
    cur = 0
    for i in operations:
        op, num = i.split()
        if op == 'D':
            if num == '1':
                if hq:
                    hq.pop(hq.index(high))
                    if hq:
                        high = max(hq)
                    else:
                        high = -math.inf
                    cur += 1
            else:
                if hq:
                    heapq.heappop(hq)
        else:
            if int(num) > high:
                high = int(num)
            heapq.heappush(hq,int(num))
    if not hq:
        return [0,0]
    else:
        return [max(hq), min(hq)]

print(solution(	["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))