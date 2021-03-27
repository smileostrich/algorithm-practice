N, target, my = map(int, input().split())
my -= 1
cur = 0
kin = 1
cnt = 0

while True:
    if kin == target:
        cnt += 1
        if cur == my:
            print(cnt)
            break
        elif cur < my:
            my -= 1
        kin = 1
        N -= 1
    else:
        kin += 1
        cur = (cur+1) % N
