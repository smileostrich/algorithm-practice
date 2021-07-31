N,S = map(int, input().split())
li_nums = list(map(int, input().split()))
cnt = 0

def back(cur, tot):
    global cnt
    if cur == N:
        if tot == S:
            cnt += 1
        return
    back(cur+1, tot)
    back(cur+1, tot+li_nums[cur])

back(0,0)
if S == 0:
    cnt -= 1
print(cnt)