N = int(input())

isused_1 = [False for _ in range(N)]
isused_2 = [False for _ in range((N-1)*2+1)]
isused_3 = [False for _ in range((N-1)*2+1)]
cnt = 0

def back(k):
    global cnt
    if k == N:
        cnt += 1
        return 0
    for i in range(N):
        if isused_1[i] or isused_2[i+k] or isused_3[k-i+N-1]:
            continue
        isused_1[i] = True
        isused_2[i+k] = True
        isused_3[k-i+N-1] = True
        back(k+1)
        isused_1[i] = False
        isused_2[i + k] = False
        isused_3[k-i + N - 1] = False
back(0)
print(cnt)