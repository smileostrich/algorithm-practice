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

if not li_odd:
    print(0)
elif N == 2:
    print('pause')
else:
    i = 0
    if li_odd == 0:
        i += 1
        cnt_result += 2
        for c in li_odd:
            while True:
                if chk_las(i):
                    cnt_result += 2
                else:

    else:
        while True:
            li_odd[i] =
    for c in li_odd:
        if chk_fir(c):
            cnt_result += 2

