# 사소한 실수로 10분 지체
# dfs 알고리즘 바꿔서 10분 지체
# 38분 1차. 디버깅시작
# dfs


# import sys
# testcase = int(sys.stdin.readline().rstrip())
# for _ in range(testcase):
#     n = int(sys.stdin.readline().rstrip())
#     choice = [0] + list(map(int, sys.stdin.readline().split()))
#     visit = [0] * (n+1)
#     group = 1
#     for i in range(1, n+1):
#         if visit[i] == 0:
#             while visit[i] == 0:
#                 visit[i] = group
#                 i = choice[i]
#             while visit[i] == group:
#                 visit[i] = -1
#                 i = choice[i]
#             group += 1
#     cnt = 0
#     for v in visit:
#         if v > 0:
#             cnt += 1
#     print(f'{cnt}')


import sys

n = int(sys.stdin.readline().rstrip())
choice = [0] + list(map(int, sys.stdin.readline().split()))
visit = [0] * (n+1)
group = 1
for i in range(1, n+1):
    if visit[i] == 0:
        while visit[i] == 0:
            visit[i] = group
            i = choice[i]
        while visit[i] == group:
            visit[i] = -1
            i = choice[i]
        group += 1
cnt = 0
for v in visit:
    if v > 0:
        cnt += 1
print(f'{cnt}')



# parent = {i: None for i in range(1, n+1)}
# for s in range(1, n+1):
#     if parent[s] == 0:
#         for neighbor in adjList[s]:
#             if neighbor not in parent:
#                 parent[neighbor] = s
#                 dfs_visit(neighbor)
