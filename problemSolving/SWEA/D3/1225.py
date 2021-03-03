from collections import deque
for _ in range(1, 11):
    tc = int(input())
    li_num = deque(map(int, input().split()))
    cur = 0
    while True:
        cur = (cur) % 5
        cur += 1
        tmp = li_num.popleft()
        tmp -= cur
        if tmp <= 0:
            li_num.append(0)
            break
        else:
            li_num.append(tmp)
    print(f'#{tc}',*li_num)