def merge(li):
    global answer
    if len(li) <= 1:
        return li
    mid = len(li) // 2
    g1 = merge(li[:mid])
    g2 = merge(li[mid:])
    result = []
    cur_1 = 0
    cur_2 = 0
    size = len(g1)
    size2 = len(g2)
    while cur_1 < size and cur_2 < size2:
        if g1[cur_1] > g2[cur_2]:
            result.append(g2[cur_2])
            cur_2 += 1
        else:
            result.append(g1[cur_1])
            cur_1 += 1
    if cur_1 < size:
        result.extend(g1[cur_1:])
        answer += 1
    if cur_2 < size2:
        result.extend(g2[cur_2:])
    return result


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    li_n = list(map(int, input().split()))
    answer = 0
    li_re = merge(li_n)
    print(f'#{tc} {li_re[N//2]} {answer}')