# 7 11
# 0 1 32
# 0 2 31
# 0 5 60
# 0 6 51
# 1 2 21
# 2 6 25
# 2 4 46
# 3 4 34
# 3 5 18
# 4 5 40
# 4 6 51

V,E = map(int,input().split())
INF = 0xfffffff
adj = [[INF]*V for _ in range(V)]
for i in range(E):
    s,e,w = map(int,input().split())
    adj[s][e] = w
    adj[e][s] = w

def prim(start):
    INF = 0xfffffff
    weight = [INF]*V
    weight[start] = 0
    mst = [0] * V
    result = 0
    st = [-1] * V
    for _ in range(V):
        print(weight)
        min_w = 0xffffff
        min_v = 0
        for i in range(V):
            if mst[i] == 0 and weight[i] < min_w:
                min_w = weight[i]
                min_v = i
        mst[min_v] = 1
        result += min_w
        for i in range(V):
            if adj[min_v][i] < weight[i] and mst[i]==0:
                weight[i] = adj[min_v][i]
                st[i] = min_v
    return result

result=prim(0)
print(result)