import sys

def back(start, depth):
    if depth == 6:
        for i in range(K):
            if li_comb[i]:
                print(li_s[i],end=' ')
        print()
        return
    for i in range(start, K):
        li_comb[i] = 1
        back(i+1, depth+1)
        li_comb[i] = 0

while True:
    tmp = list(map(int, sys.stdin.readline().split()))
    if len(tmp) == 1:
        break
    K, li_s = tmp[0], tmp[1:]
    li_comb = [0]*K
    back(0,0)
    print()
