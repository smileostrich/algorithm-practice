TC = int(input())

for tc in range(1, TC+1):
    N,M = map(int, input().split())
    data = list(map(int, input().split()))
    Q = []
    for i in range(N):
        Q.append([data[i], i])
    i = 0
    while len(Q)!=1:
        Q[0][0] //= 2

        if Q[0][0] == 0:
            if N+ i < M:
                Q.pop(0)
                Q.append([data[N+i], N+i])
                i+=1
            elif N+i >= M:
                Q.pop(0)
        else:
            Q.append(Q.pop(0))
    print(f'#{tc} {Q[0][1]+1}')

# from collections import deque
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N,M = map(int, input().split())
#     li_pizza = map(int, input().split())
#     dq_pizza = deque([[idx+1, i] for idx, i in enumerate(li_pizza)])
#     dq_grill = deque([])
#     for _ in range(N):
#         dq_grill.append(dq_pizza.popleft())
#     while len(dq_grill) > 1:
#         if dq_grill[0][1] == 0:
#             dq_grill.popleft()
#             if dq_pizza:
#                 dq_grill.appendleft(dq_pizza.popleft())
#         dq_grill[0][1] //= 2
#         dq_grill.append(dq_grill.popleft())
#     print(f'#{tc} {dq_grill[0][0]}')