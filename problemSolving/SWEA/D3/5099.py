from collections import deque


T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    li_pizza = map(int, input().split())
    dq_pizza = deque([[idx+1, i]for idx, i in enumerate(li_pizza)])
    dq_grill = deque([])
    for _ in range(N):
        dq_grill.append(dq_pizza.popleft())
    while len(dq_grill) > 1:
        if dq_grill[0][1] == 0:
            dq_grill.popleft()
            if dq_pizza:
                dq_grill.appendleft(dq_pizza.popleft())
        else:
            dq_grill[0][1] //= 2
        dq_grill.append(dq_grill.popleft())
    print(f'#{tc} {dq_grill[0][0]}')