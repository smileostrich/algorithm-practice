from collections import deque

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    li_a = sorted(list(map(int, input().split())))
    d_a = deque(li_a)
    li_result = []
    for i in range(10):
        if i % 2 == 0:
            li_result.append(d_a.pop())
        else:
            li_result.append(d_a.popleft())
    print(f'#{tc}', *li_result)