# 중간에 개인적인 일(코딩x)로 시간 제대로 측정안됨
import heapq
import math


mat = [[1,2,3],[4,5,6],[7,8,9],[-1,0,-2]]
vList = [1,2,3,4,5,6,7,8,9,-1,0,-2]
adjList = {1: [(2, 1), (4, 1)], 2: [(1,1), (5,1),(3,1)], 3:[(2,1),(6,1)], 4: [(1,1), (5,1),(7,1)], 5:[(2,1),(4,1),(6,1),(8,1)], 6:[(3,1),(5,1),(9,1)], 7:[(4,1),(8,1),(-1,1)], 8:[(5,1),(7,1),(9,1),(0,1)], 9:[(6,1),(8,1),(-2,1)], -1:[(7,1),(0,1)], 0:[(8,1),(-1,1),(-2,1)], -2:[(9,1),(0,1)]}

def solution(numbers, hand):
    left_list = [1,4,7]
    right_list = [3,6,9]
    middle_list = [2,5,8,0]

    cur_left = -1
    cur_right = -2
    answer = ''

    for target_n in numbers:
        if target_n in left_list:
            cur_left = target_n
            answer += 'L'
        elif target_n in right_list:
            cur_right = target_n
            answer += 'R'
        else:
            r1 = shortest_path(cur_left, target_n)
            r2 = shortest_path(cur_right, target_n)
            if r1 == r2:
                if hand == 'right':
                    cur_right = target_n
                    answer += 'R'
                else:
                    cur_left = target_n
                    answer += 'L'
            elif r1 > r2:
                cur_right = target_n
                answer += 'R'
            else:
                cur_left = target_n
                answer += 'L'
    return answer


def dijkstra(adjList, s):
    pqueue = []
    dist = {i:math.inf for i in vList}
    parent = {i:None for i in vList}
    dist[s] = 0

    def relax(u, v, w):
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            heapq.heappush(pqueue, (dist[v], v))
            parent[v] = u

    for v in vList:
        heapq.heappush(pqueue, (dist[v], v))

    while pqueue:
        k, u = heapq.heappop(pqueue)
        if k <= dist[u]:
            for v, w in adjList[u]:
                relax(u, v, w)

    return dist, parent


def shortest_path(s, e):
    dist, parent = dijkstra(adjList, s)
    path = [e]
    current = e
    cost = 0
    while parent[current]:
        path.insert(0, parent[current])
        current = parent[current]
    for v in path:
        cost = dist[v]
    # print(f'path:{path}cost:{cost}')
    return cost


# 실해ㅑㅇ
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))