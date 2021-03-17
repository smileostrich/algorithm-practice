T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    li_sq = []
    lowx,lowy,hix,hiy = 301,301,0,0
    for _ in range(N):
        x1,y1,x2,y2 = map(int, input().split())
        if x2 > x1:
            if y2 > y1:
                sx, sy, bx, by = x1,y1,x2,y2
            else:
                sx, sy, bx, by = x1,y2,x2,y1
        else:
            if y2 > y1:
                sx, sy, bx, by = x2,y1,x1,y2
            else:
                sx, sy, bx, by = x2,y2,x1,y1
        if bx > hix:
            hix = bx
        if by > hiy:
            hiy = by
        if sx < lowx:
            lowx = sx
        if sy < lowy:
            lowy = sy
        li_sq.append([sx,sy,bx,by])
    # siz = max((hix-lowx),(hiy-lowy))
    siz = 300
    result = 0
    for k in range(1, siz+1):
        if result != 0:
            break
        for y in range(lowy,siz+1-k):
            if result != 0:
                break
            for x in range(lowx, siz+1-k):
                cnt = 0
                for sx,sy,bx,by in li_sq:
                    if x <= sx and y <= sy and x+k >= bx and y+k >= by:
                        cnt += 1
                if N-cnt <= M:
                    result = k
                    print(f'#{tc} {result}')
                    break
    # print(f'#{tc} {result}')