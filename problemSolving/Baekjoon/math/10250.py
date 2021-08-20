T = int(input())
for _ in range(T):
    H,W,N = map(int, input().split())
    h = ''
    r = ''

    if N%H == 0:
        if N //H < 10:
            r = '0' + str(N // (H))
        else:
            r = str(N // (H))
        h=str(H)
    else:
        if N // H + 1 < 10:
            r = '0' + str(N // (H) + 1)
        else:
            r = str(N // (H) + 1)
        h=str(N%H)
    print(h+r)