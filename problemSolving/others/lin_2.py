
maze = [[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]
size = len(maze)
# [0, 1, 0, 1],
# [0, 1, 0, 0],
# [0, 0, 0, 0],
# [1, 0, 1, 0]

face = [(1,0),(0,1),(0,-1),(-1,0)]
cur = 0
def test(s):
    global cur
    frontier = [s]
    i = 0
    while frontier:
        next = []
        for x, y in frontier:
            # for new_x,new_y in face:
            c_x, c_y = x, y
            while True:
                x, y = c_x, c_y
                if cur == 0:
                    new_x, new_y = 0, -1
                elif cur == 1:
                    new_x, new_y = 1, 0
                elif cur == 2:
                    new_x, new_y = 0, 1
                elif cur == 3:
                    new_x, new_y = -1, 0
                x, y = x + new_x, y + new_y
                if 0 <= y < size and 0 <= x < size and maze[y][x] != 1:
                    cur = (cur + 3) % 4
                    next.append((x,y))
                    break
                # elif 0 <= y < size and 0 <= x < size and maze[y][x] == 1:
                #     cur = (cur + 1) % 4
                # if 0 <= y < size and 0 <= x < size:
                #     if maze[y][x] != 1:
                #         next.append((x,y))
                #         break
                #     else:
                #         cur = (cur + 1) % 4
                else:
                    cur = (cur+1) % 4
        frontier = next
        i += 1
    print(i)
    print(frontier)

test((0,0))
# def BFS(s):
#     level = {s: 0}
#     parent = {s: None}
#     i = 1
#     frontier = [s]
#     while frontier:
#         next = []
#         for u in frontier:
#             for v in adj[u]:
#                 if v not in level:
#                     level[v] = i
#                     parent[v] = u
#                     next.append(v)
#         frontier = next
#         i += 1
#     print(i)
#     print(frontier)
#     print(parent)
#     print(level)
#
# BFS(1)