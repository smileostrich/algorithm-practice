n = int(input())
c = list(map(int,input().rstrip("\n")))
want = list(map(int,input().rstrip("\n")))

def change(num):
    if num == 0:
        num = 1
    else:
        num = 0
    return num

def switch(c, cnt):
    count = cnt
    if count == 1:
        c[0] = change(c[0])
        c[1] = change(c[1])
    for i in range(1, n):
        if c[i-1] != want[i-1]:
            count += 1
            c[i-1] = change(c[i-1])
            c[i] = change(c[i])
            if i != n-1:
                c[i+1] = change(c[i+1])
    if c == want:
        return count
    else:
        return -1

res1 = switch(c[:], 0)
res2 = switch(c[:], 1)
if res1 >= 0 and res2 >= 0:
    print(min(res1, res2))
elif res1>=0 and res2 < 0:
    print(res1)
elif res1 <0 and res2 >= 0:
    print(res2)
else:
    print(-1)


# 실패 소스
# from sys import stdin
#
#
# inp = lambda: stdin.readline().rstrip()
#
# N = inp()
# cur_bulb = inp()
# ideal_bulb = inp()
# li_odd = []
#
# for idx, tu in enumerate(zip(cur_bulb, ideal_bulb)):
#     a, b = tu
#     if a != b:
#         li_odd.append(idx)
#
# def chk_fir(n):
#     if n == 0:
#         return True
#     else:
#         return False
#
# def chk_las(n):
#     if N-1 == n:
#         return True
#     else:
#         return False
#
# cnt_result = 0
# bool_result = 0
# if not li_odd:
#     print(0)
# elif N == 2:
#     print('pause')
# else:
#     i = 0
#     if li_odd == 0:
#         cur_bulb[i] = 1 - cur_bulb[i]
#         # cur_bulb[i+1] = 1 - cur_bulb[i+1]
#         cnt_result += 1
#         i += 1
#     while True:
#         if chk_las(i):
#             if cur_bulb[i-1] != ideal_bulb[i-1]:
#                 bool_result = -1
#             else:
#                 cnt_result += 2
#             break
#         else:
#             cur_bulb[i] = 1 - cur_bulb[i]
#             cnt_result += 2
#             i += 1
# if bool_result == -1:
#     print(-1)
# else:
#     print(cnt_result)
