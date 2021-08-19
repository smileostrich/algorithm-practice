N = int(input())

s = 1
k = 6
cnt = 1
while s < N:
    s += k
    k += 6
    cnt += 1
print(cnt)