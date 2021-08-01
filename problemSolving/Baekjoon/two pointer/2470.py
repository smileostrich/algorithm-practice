N = int(input())
li_n = list(map(int, input().split()))
li_n.sort()

left, right = 0, N-1
lowest = 100000000000
li_result = []
while left < right:
    # if li_n[left] > 0 or li_n[right] < 0:
    #     break
    tmp = li_n[left] + li_n[right]
    if abs(tmp) < lowest:
        lowest = abs(tmp)
        li_result = [str(li_n[left]), str(li_n[right])]
    if tmp > 0:
        right -= 1
    else:
        left += 1
print(' '.join(li_result))