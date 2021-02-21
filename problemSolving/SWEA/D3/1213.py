for _ in range(10):
    tc = int(input())
    base = input()
    target = input()

    size = len(target)-len(base)
    l_size = len(base)
    cur = 0
    cnt = 0
    while cur <= size:
        if target[cur:cur+l_size] == base:
            cnt += 1
        cur += 1
    print(f'#{tc} {cnt}')