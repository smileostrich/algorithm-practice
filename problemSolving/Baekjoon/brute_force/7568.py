N = int(input())
li_p = [tuple(map(int, input().split())) for _ in range(N)]
for i in li_p:
    rank = 1
    for j in li_p:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')