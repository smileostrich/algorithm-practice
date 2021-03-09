# 풀이 1
# answer = 0
# def DFS(idx, numbers, target, value):
#     global answer
#     N = len(numbers)
#     if(idx== N and target == value):
#         answer += 1
#         return
#     if(idx == N):
#         return
#     DFS(idx+1,numbers,target,value+numbers[idx])
#     DFS(idx+1,numbers,target,value-numbers[idx])
#
#
# def solution(numbers, target):
#     global answer
#     DFS(0,numbers,target,0)
#     return answer

# 풀이 2
def solution(numbers, target):
    answer = 0
    queue = [(0, 0)]
    length = len(numbers)

    while queue:
        n = queue.pop()
        if n[0] < length:
            queue.append((n[0] + 1, n[1] + numbers[n[0]]))
            queue.append((n[0] + 1, n[1] - numbers[n[0]]))
        elif n[1] == target:
            answer += 1

    return answer

print(solution([1,1,1,1,1],3))