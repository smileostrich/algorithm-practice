def back(idx, cnt, left):
    global low
    if low > cnt:
        if idx == N-1:
            if low > cnt:
                low = cnt
            return
        else:
            if left == 0:
                back(idx+1, cnt+1, li_battery[idx]-1)
            else:
                back(idx+1, cnt+1, li_battery[idx]-1)
                back(idx+1, cnt, left-1)

T = int(input())
for tc in range(1, T + 1):
    li_m = list(map(int, input().split()))
    N, li_battery = li_m[0], li_m[1:]
    low = len(li_battery)+2
    back(1,0,li_battery[0]-1)

    print(f'#{tc} {low}')