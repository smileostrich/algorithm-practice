while True:
    x,y,h = map(int,input().split())
    if x == y == h == 0:
        break
    li_p = sorted([x,y,h])
    if li_p[0]**2+li_p[1]**2 == li_p[-1]**2:
        print('right')
    else:
        print('wrong')