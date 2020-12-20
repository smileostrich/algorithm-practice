import sys


dat = {1:[1], 2:[6,2,4,8], 3:[1,3,9,7], 4:[6,4], 5:[5], 6:[6], 7:[1,7,9,3], 8:[6,8,4,2], 9:[1,9], 0:[10]}

T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    last_num = int(str(a)[-1])
    dat_len = len(dat[last_num])
    re = dat[last_num][b % dat_len]
    print(re)


# already sovled