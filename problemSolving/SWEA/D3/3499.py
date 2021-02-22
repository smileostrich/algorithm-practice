from collections import deque
T = int(input())
# T = 1
for tc in range(1, T+1):
    N = int(input())
    # N = 6
    li_card = list(input().split())
    size = len(li_card)
    result = []
    if size % 2 == 1:
        mid = size // 2 + 1
        li_fir = deque(li_card[:mid])
        li_las = deque(li_card[mid:])
        while len(li_fir) and len(li_las):
            result.append(li_fir.popleft())
            result.append(li_las.popleft())
        result.append(li_fir.pop())
    else:
        mid = size // 2
        li_fir = deque(li_card[:mid])
        li_las = deque(li_card[mid:])
        while len(li_fir) and len(li_las):
            result.append(li_fir.popleft())
            result.append(li_las.popleft())
    print(f'#{tc}', *result)