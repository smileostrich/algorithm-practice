from collections import deque
from collections import defaultdict

def solution(info, edges):
    dic_adj = {i:[] for i in range(len(info))}

    for v1, v2 in edges:
        dic_adj[v1].append(v2)
    level = {0: 0}
    group_level = defaultdict(list)
    i = 1
    queue = [0]
    dic_cnt = {i:0 for i in range(len(info))}
    dic_cnt[0] = 1
    group_cnt = defaultdict(list)
    group_cnt[0] = [1]
    while queue:
        next = []
        for u in queue:
            for neighbor in dic_adj[u]:
                if neighbor not in level:
                    level[neighbor] = i
                    if info[neighbor]:
                        dic_cnt[neighbor] += dic_cnt[u]-1
                        group_level[i].append(neighbor)
                        group_cnt[i].append(dic_cnt[u]-1)
                    else:
                        dic_cnt[neighbor] += dic_cnt[u] + 1
                        group_level[i].append(neighbor)
                        group_cnt[i].append(dic_cnt[u]+1)
                    next.append(neighbor)
        queue = next
        i += 1
    print(dic_cnt)
    print(group_level)
    print(group_cnt)
    sheep = 1
    wolf = 0
    # for k, v in group_cnt.items():
    #     if k <= sheep:
    #         # wolf +=
    #     else:
    #         break
    return sheep

    # while queue:
    #     next = []
    #     for u in queue:
    #         for neighbor in dic_adj[u]:
    #             if neighbor not in level:
    #                 level[neighbor] = i
    #                 if info[neighbor]:
    #                     group_level[i].append(0)
    #                 else:
    #                     group_level[i].append(1)
    #                 next.append(neighbor)
    #     queue = next


    # print(level)




# print(solution(	[0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
print(solution(	[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))