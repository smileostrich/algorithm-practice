N,S = map(int, input().split())
li_su = list(map(int, input().split()))
left, right = 0, 0
tmp_sum = 0
sm = 1000001

while True:
    if tmp_sum >= S:
        sm = min(sm, right-left)
        tmp_sum -= li_su[left]
        left += 1
    elif right == N:
        break
    else:
        tmp_sum += li_su[right]
        right += 1

if sm == 1000001:
   print(0)
else:
   print(sm)