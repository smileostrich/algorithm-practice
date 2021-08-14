from collections import deque


N, K = map(int, input().split())
li_visited = [-1 for _ in range(max(N,K)*2+1)]
q = deque([(N,0)])
lowest = 1000000000

while q:
    pos, cnt = q.popleft()
    if cnt < lowest:
        if pos == K:
            if lowest > cnt:
                lowest = cnt
        for next in (pos-1, pos+1, pos*2):
            if 0<=next<len(li_visited) and li_visited[next] == -1:
                li_visited[next] = cnt
                q.append((next, cnt+1))
print(lowest)

# while q:
#     pos, cnt = q.popleft()
#     if pos == K:
#         if lowest > cnt:
#             lowest = cnt
#         continue
#     elif 0<=pos<len(li_visited) and cnt < lowest:
#         if li_visited[pos] == -1:
#             li_visited[pos] = cnt
#         elif li_visited[pos] > cnt:
#             continue
#         else:
#             li_visited[pos] = cnt
#         # if 2*pos <= K:
#         #     q.append((pos*2,cnt+1))
#         # else:
#         q.append((pos * 2, cnt + 1))
#         q.append((pos + 1, cnt + 1))
#         q.append((pos - 1, cnt + 1))
# print(lowest)