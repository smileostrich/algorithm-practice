from collections import deque


def bfs(s):
    level = {s: 0}
    i = 1
    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            for v in adjlist[u]:
                if v not in level:
                    level[v] = i
                    next.append(v)
        frontier = next
        i += 1
    return level


T = int(input())
for tc in range(1, T+1):
    V,E = map(int, input().split())
    adjlist = {i+1:[] for i in range(V)}
    for _ in range(E):
        s1,s2 = map(int, input().split())
        adjlist[s1].append(s2)
        adjlist[s2].append(s1)
    sv, ev = map(int, input().split())
    res = bfs(sv)
    if ev in res:
        print(f'#{tc} {res[ev]}')
    else:
        print(f'#{tc} 0')