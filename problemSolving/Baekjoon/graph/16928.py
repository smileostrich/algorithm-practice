from collections import deque

N, M = map(int, input().split())
# board_cnt = [0] * 101
li_visited = [False] * 101
dic_snake = {}
dic_ladder = {}
for _ in range(N):
    i, j = map(int, input().split())
    dic_ladder[i] = j
for _ in range(M):
    i, j = map(int, input().split())
    dic_snake[i] = j

lowest = 1000000

queue = deque([(1,0)])
while queue:
    pos, cnt = queue.popleft()
    if pos == 100:
        if lowest > cnt:
            lowest = cnt
    for i in range(1,7):
        if pos+i <= 100 and not li_visited[pos+i]:
            if pos+i in dic_snake:
                li_visited[pos + i] = True
                li_visited[dic_snake[pos + i]] = True
                queue.append((dic_snake[pos + i], cnt + 1))
            elif pos+i in dic_ladder:
                li_visited[pos+i] = True
                li_visited[dic_ladder[pos+i]] = True
                queue.append((dic_ladder[pos+i],cnt+1))
            else:
                li_visited[pos + i] = True
                queue.append((pos+i, cnt + 1))
print(lowest)