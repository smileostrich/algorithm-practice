def bfs(cnt):
    global high
    if not cnt:
        tmp = int(''.join(li_numbers))
        if high < tmp:
            high = tmp
        return
    else:
        for i in range(len(li_numbers)):
            for j in range(i+1, len(li_numbers)):
                li_numbers[i], li_numbers[j] = li_numbers[j], li_numbers[i]
                cur = ''.join(li_numbers)
                if visited.get((cur, cnt-1), 1):
                    visited[(cur, cnt-1)] = 0
                    bfs(cnt-1)
                li_numbers[i], li_numbers[j] = li_numbers[j], li_numbers[i]

T = int(input())
for tc in range(1, T+1):
    numbers, n_exchange = map(int, input().split())
    li_numbers = []
    for i in str(numbers):
        li_numbers.append(i)
    visited = {}
    high = 0
    bfs(n_exchange)
    print(f'#{tc} {high}')