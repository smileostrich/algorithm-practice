def bin_search(l,r,A):
    mid = (l+r)//2
    if mid == A:
        return 1
    else:
        if mid > A:
            return 1 + bin_search(l, mid, A)
        else:
            return 1 + bin_search(mid, r, A)

T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    result = ''

    if A == P:
        A = 0
    else:
        A = bin_search(1,P,A)
    if B == P:
        B = 0
    else:
        B = bin_search(1,P,B)

    if A == B:
        result = 0
    elif A > B:
        result = 'B'
    else:
        result = 'A'

    print(f'#{tc} {result}')