from collections import deque
from copy import deepcopy

def solution(tickets):
    ans = []
    dic_ticket = {}
    size = len(tickets)
    for i in tickets:
        if i[0] in dic_ticket:
            dic_ticket[i[0]].append(i[1])
        else:
            dic_ticket[i[0]] = [i[1]]
    for k in dic_ticket.keys():
        dic_ticket[k] = sorted(dic_ticket[k], reverse=True)
    q = deque([])
    q.append((0,['ICN'], deepcopy(dic_ticket)))
    while q:
        cur = q.popleft()
        if cur[0] < size:
            ticket = cur[1][-1]
            if ticket in cur[2]:
                for i in range(len(cur[2][ticket])):
                    tmp = deepcopy(cur[1])
                    tmp2 = deepcopy(cur[2])
                    tmp.append(tmp2[ticket].pop(i))
                    q.append((cur[0] + 1, tmp, tmp2))
        elif cur[0] == size:
            ans.append(cur[1])
    return sorted(ans)[0]





print(solution(	[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution(	[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))


# from collections import defaultdict
#
# def dfs(graph, N, key, footprint):
#     print(footprint)
#
#     if len(footprint) == N + 1:
#         return footprint
#
#     for idx, country in enumerate(graph[key]):
#         graph[key].pop(idx)
#
#         tmp = footprint[:]
#         tmp.append(country)
#
#         ret = dfs(graph, N, country, tmp)
#
#         graph[key].insert(idx, country)
#
#         if ret:
#             return ret
#
#
# def solution(tickets):
#     answer = []
#
#     graph = defaultdict(list)
#
#     N = len(tickets)
#     for ticket in tickets:
#         graph[ticket[0]].append(ticket[1])
#         graph[ticket[0]].sort()
#
#     answer = dfs(graph, N, "ICN", ["ICN"])
#
#     return answer