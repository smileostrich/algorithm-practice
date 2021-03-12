dic_level = {}

def bfs_visit(s):
    global dic_adj
    global dic_parent
    global dic_child
    frontier = [s]
    while frontier:
        next = []
        for cur in frontier:
            for neighbor in dic_adj[cur]:
                dic_parent[neighbor].append(cur)
                dic_child[cur].append(neighbor)
                next.append(neighbor)
        frontier = next


def bfs(n):
    for s in range(1, n+1):
        bfs_visit(s)


def solution(n, results):
    global dic_adj
    global dic_parent
    global dic_child
    dic_adj = {i:[] for i in range(1,n+1)}
    dic_child = {i: [] for i in range(1, n + 1)}
    for a,b in results:
        dic_adj[a].append(b)
    dic_parent = {i:[] for i in range(1,n+1)}
    bfs(n)
    for i in dic_parent.keys():
        set(dic_parent[i])
    for i in dic_child.keys():
        set(dic_parent[i])
    return dic_parent

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))