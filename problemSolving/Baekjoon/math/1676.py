N=int(input())
ans = 0
cnt_two = 0
cnt_five = 0
for i in range(2,N+1):
    while True:
        if i % 2 == 0:
            cnt_two += 1
            i //= 2
            continue
        elif i % 5 == 0:
            cnt_five += 1
            i //= 5
            continue
        else:
            break
print(min(cnt_two,cnt_five))