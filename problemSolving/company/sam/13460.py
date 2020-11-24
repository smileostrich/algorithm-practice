# 입력까지 3분
# 문제이해까지 7분
# 인풋까지 11분
# 이해 잘못 20분
# 전처리 23분
# 테스트 25분
# 다시 전처리 30분
import sys


N, M = map(int, sys.stdin.readline().split())
# mat = [sys.stdin.readline()[1:M-1] for _ in range(M)]
# pre_mat = mat[1:-1]
mat = [0] * (M-1)
RGB = ['R', 'G', 'B']

for i in range(N-1):
    if i == 0:
        sys.stdin.readline()
        continue
    test = sys.stdin.readline()[1:M]
    tmp = list(map(str, sys.stdin.readline()[1:M].split()))
    test.
    if RGB in tmp:
    mat[i] = tmp

new_mat = mat[1:]


def BFS(s):
    level = {s: 0}
    parent = {s: None}
    i = 1
    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        frontier = next
        i += 1
    print(i)
    print(frontier)
    print(parent)
    print(level)

BFS()