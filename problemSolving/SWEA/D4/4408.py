from itertools import permutations
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li_room = [0 for i in range(400+1)]
    for _ in range(N):
        l, r = map(int, input().split())
        if l % 2 == 1:
            l += 1
        if r % 2 == 1:
            r += 1
        if l > r:
            for j in range(r, l+1):
                li_room[j] += 1
        elif l == r:
            continue
        else:
            for j in range(l,r+1):
                li_room[j] += 1
    print(f'#{tc} {max(li_room)}')


    # small = 400
    # high = 0
    #
    # for i in range(N):
    #     tmp = list(map(int, input().split()))
    #     l, r = tmp
    #     if l < small:
    #         small = l
    #     if r > high:
    #         high = r
    #     matrix.append(tmp)
    #
    # li_room



    # matrix = [(10, 20), (30, 40), (50, 60), (70, 80)]
    # # matrix = []
    # # for i in range(N):
    # # matrix.append(tuple(map(int, input().split())))
    # for i in permutations(matrix, N):
    #     cnt = 0
    #     stack = list(i)
    #     k, v = stack.pop()
    #     for j in i:
    #         tk, tv = j
    #         if k >
    #     # for j in stack:
    #     #     if s_k
    #     # stack.append(i)