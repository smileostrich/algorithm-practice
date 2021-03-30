from itertools import combinations_with_replacement
nums = [1, 5, 10, 50]
N = int(input())
result = []
for comb in combinations_with_replacement(range(4), N):
    sum_tmp = 0
    for i in comb:
        sum_tmp += nums[i]
    if sum_tmp not in result:
        result.append(sum_tmp)
print(len(result))

# from collections import deque
#
#
# N = int(input())
# li_test = [1,5,10,50]
#
# dq = deque([(0,0)])
# visited = [False for _ in range(N*50+1)]
# cnt = 0
# while dq:
#     idx, cur = dq.popleft()
#     if idx == N:
#         if not visited[cur]:
#             visited[cur] = True
#             cnt += 1
#     elif idx < N:
#         for i in li_test:
#             if not visited[cur+i]:
#                 dq.append((idx+1, i+cur))
# print(cnt)

# from collections import deque
#
#
# N = int(input())
# li_test = [1,5,10,50]
#
# dq = deque([(0,0)])
# visited = [[False for _ in range(N*50+1)] for _ in range(N+1)]
# cnt = 0
# while dq:
#     idx, cur = dq.popleft()
#     if idx == N:
#         if not visited[idx][cur]:
#             visited[idx][cur] = True
#             cnt += 1
#     elif idx < N:
#         for i in li_test:
#             if not visited[idx+1][cur+i]:
#                 dq.append((idx+1, i+cur))
# print(cnt)