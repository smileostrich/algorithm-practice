# 네모를 첫번째
# 나머지면, 2차원 배열 회전

from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().rstrip().split())
mat = [[0] for _ in range(N)]
for i in range(N):
    mat[i] = list(map(int, stdin.readline().rstrip().split()))


def rotate_array(arr):
    return list(zip(*reversed(arr)))


def mirror_array(arr):
    return [reversed(i) for i in arr]


poliomino = []

pol_1 = [(0,0), (1,0), (2,0), (3,0)]
poliomino.append(pol_1)
poliomino.append(rotate_array(pol_1))

pol_2 = [(0,0), (0,1), (1,0), (1,1)]
poliomino.append(pol_1)

pol_3 = [(0,0), (0,1), (0,2), (1,2)]
poliomino.append(pol_3)
poliomino.append(rotate_array(pol_3))
poliomino.append(rotate_array(rotate_array(pol_3)))
poliomino.append(rotate_array(rotate_array(rotate_array(pol_3))))
poliomino.append(rotate_array(rotate_array(rotate_array(rotate_array(pol_3)))))
poliomino.append(mirror_array(pol_3))
poliomino.append(rotate_array(mirror_array(pol_3)))
poliomino.append(rotate_array(rotate_array(mirror_array(pol_3))))
poliomino.append(rotate_array(rotate_array(rotate_array(mirror_array(pol_3)))))
poliomino.append(rotate_array(rotate_array(rotate_array(rotate_array(mirror_array(pol_3))))))

pol_4 = [(0,0), (0,1), (1,1), (1,2)]
poliomino.append(pol_4)
poliomino.append(rotate_array(pol_4))
pol_4_mirror = mirror_array(pol_4)
poliomino.append(pol_4_mirror)
poliomino.append(rotate_array(pol_4_mirror))

pol_5 = [(0,0), (1,0), (1,1), (2,0)]
poliomino.append(pol_5)
poliomino.append(rotate_array(pol_5))
poliomino.append(rotate_array(rotate_array(pol_5)))
poliomino.append(rotate_array(rotate_array(rotate_array(pol_5))))
poliomino.append(rotate_array(rotate_array(rotate_array(rotate_array(pol_5)))))

mov = [(1,0), (0,1)]

def bfs(pol):
    q = deque()
    q.append(pol)
    result = 0
    while q:
        # b_check = True
        cur_pol = q.pop()
        for i in reversed(cur_pol):
            for x, y in mov:
                new_x, new_y = cur_x + x, cur_y + y
                q.popleft()


for p in poliomino:
    bfs(p)
