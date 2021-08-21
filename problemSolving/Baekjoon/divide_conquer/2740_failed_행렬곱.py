ay,ax = map(int, input().split())
li_mata = [list(map(int, input().split())) for _ in range(ay)]
by,bx = map(int, input().split())
li_matb = [list(map(int, input().split())) for _ in range(by)]
li_result = [[0 for _ in range(bx)] for _ in range(ay)]
for q in range(ay):
    for w in range(bx):
        for e in range(ax):
            li_result[q][w] += li_mata[q][e] * li_matb[e][w]
for i in li_result:
    print(*i)





