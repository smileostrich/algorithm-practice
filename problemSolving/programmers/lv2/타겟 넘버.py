from collections import deque


def solution(numbers, target):
    answer = 0
    dq = deque([(0,0)])
    size = len(numbers)
    while dq:
        cur = dq.popleft()
        if cur[0] < size:
            dq.append((cur[0]+1, cur[1] + numbers[cur[0]]))
            dq.append((cur[0] + 1, cur[1] - numbers[cur[0]]))
        elif cur[1] == target:
            answer += 1
    return answer


print(solution([1,1,1,1,1],3))