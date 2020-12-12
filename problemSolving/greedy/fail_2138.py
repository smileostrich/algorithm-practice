from sys import stdin


inp = lambda: stdin.readline().rstrip()

N = inp()
cur_bulb = inp()
ideal_bulb = inp()
li_odd = []

for idx, tu in enumerate(zip(cur_bulb, ideal_bulb)):
    a, b = tu
    if a != b:
        li_odd.append(idx)

def chk_fir(n):
    if n == 0:
        return True
    else:
        return False

def chk_las(n):
    if N-1 == n:
        return True
    else:
        return False

cnt_result = 0
bool_result = 0
if not li_odd:
    print(0)
elif N == 2:
    print('pause')
else:
    i = 0
    if li_odd == 0:
        cur_bulb[i] = 1 - cur_bulb[i]
        # cur_bulb[i+1] = 1 - cur_bulb[i+1]
        cnt_result += 1
        i += 1
    while True:
        if chk_las(i):
            if cur_bulb[i-1] != ideal_bulb[i-1]:
                bool_result = -1
            else:
                cnt_result += 2
            break
        else:
            cur_bulb[i] = 1 - cur_bulb[i]
            cnt_result += 2
            i += 1
if bool_result == -1:
    print(-1)
else:
    print(cnt_result)
