import sys

def bfs(queue):
    k = 0
    while queue:
        next = []
        for a, b in queue:
            for dx, dy in near:
                newX, newY = a+dx, b+dy
                if (0 <= newY < N) and (0 <= newX < M) and (mat[newY][newX] == 0):
                    next.append((newX, newY))
                    mat[newY][newX] = 1
        queue = next
        k += 1

    for i in mat:
        if 0 in i:
            return -1
    return k-1


M, N = map(int, sys.stdin.readline().split())
mat = [[] for _ in range(N)]
near = [(1, 0), (0, 1), (0, -1), (-1, 0)]
queue = []
for i in range(N):
   mat[i] = list(map(int, sys.stdin.readline().split()))
   for idxj, j in enumerate(mat[i]):
       if j == 1:
           queue.append((idxj,i))
print(bfs(queue))
