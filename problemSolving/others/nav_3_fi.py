from collections import deque
def test(n, edges):
    dic_adj = {i:[] for i in range(n)}
    for e1,e2 in edges:
        dic_adj[e1].append(e2)
    visited = [False for _ in range(n)]
    dq = deque([0])
    cnt_result = 1
    while dq:
        cur = dq.popleft()
        cnt_inner = []
        for neighbor in dic_adj[cur]:
            if not visited[neighbor]:
                inner_dq = deque([neighbor])
                inner_visited = [False for _ in range(n)]
                cnt = 0
                while inner_dq:
                    inner_cur = inner_dq.popleft()
                    for inner_n in dic_adj[inner_cur]:
                        if not inner_visited[inner_n]:
                            cnt += 1
                            inner_dq.append(inner_n)
                    inner_visited[inner_cur] = True
                cnt_inner.append(cnt)
        highest = -1
        h_idx = -1
        for idx, val in enumerate(cnt_inner):
            if highest < val:
                h_idx = dic_adj[cur][idx]
                highest = val
        for di_cur in dic_adj[cur]:
            if di_cur != h_idx:
                dq.append(di_cur)
                cnt_result += 1
    return cnt_result


# print(test(19, [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [6, 16], [8, 17], [8, 18]]))
# print(test(14, [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[2,7],[3,8],[3,9],[3,10],[4,11],[4,12],[4,13]]))
print(test(10, [[0,1],[0,2],[1,3],[2,4],[2,5],[2,6],[3,7],[3,8],[3,9]]))