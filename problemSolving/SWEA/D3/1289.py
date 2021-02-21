T = int(input())
for tc in range(1, T+1):
    target = list(input())
    size = len(target)
    origin = '0'*size
    made = ''
    cnt = 0
    for i in range(size):
        if target[i] != origin[i]:
            cnt += 1
            origin = origin[:i+1] + target[i]*(size-i)
    print(f'#{tc} {cnt}')