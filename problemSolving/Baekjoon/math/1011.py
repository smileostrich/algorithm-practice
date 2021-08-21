from collections import deque

T = int(input())

for _ in range(T):
    x,y = map(int, input().split())
    y -= 1
    y -= x
    if y == 0:
        print(1)
    else:
        li_d = [0 for _ in range(y)]
        q = deque([(1, 1)])
        while q:
            c, idx = q.popleft()
            if c == y-1:
                print(idx)
                break
            cnt = c
            ap = idx
            while cnt <= y:
                if not li_d[cnt]:
                    li_d[cnt] = ap
                    q.append((cnt, ap))
                cnt += ap
                ap += 1