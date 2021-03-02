def winner(v1, v2):
    fir, sec = v1[1], v2[1]
    if fir == 1 and sec == 2:
        winner = v2
    elif fir == 1 and sec == 3:
        winner = v1
    elif fir == 2 and sec == 1:
        winner = v1
    elif fir == 2 and sec == 3:
        winner = v2
    elif fir == 3 and sec == 1:
        winner = v2
    elif fir == 3 and sec == 2:
        winner = v1
    else:
        winner = v1
    return winner


def rec(N, li):
    if N == 1:
        return li[0]
    mid = N//2
    if N % 2 == 1:
        return winner(rec(mid+1, li[:mid + 1]), rec(mid, li[mid+1:]))
    else:
        return winner(rec(mid,li[:mid]), rec(mid, li[mid:]))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li_card = []
    for idx, i in enumerate(map(int, input().split())):
        li_card.append((idx+1, i))
    print(f'#{tc} {rec(N,li_card)[0]}')