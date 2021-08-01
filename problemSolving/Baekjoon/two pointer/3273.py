N = int(input())
li_n = list(map(int, input().split()))
X = int(input())
li_n.sort()
left, right = 0, N-1
cnt = 0
while left < right:
    temp = li_n[left] + li_n[right]
    if temp == X:
        cnt += 1
        left += 1
    elif temp < X:
        left += 1
    else:
        right -= 1
print(cnt)