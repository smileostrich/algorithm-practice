N, C = map(int, input().split())
li_items = list(map(int, input().split()))
li_a = li_items[:N//2]
li_b = li_items[N//2:]
sum_a = []
sum_b = []

def bruteforce(li_w, li_sum, l, w):
    if l >= len(li_w):
        li_sum.append(w)
        return
    bruteforce(li_w, li_sum, l+1, w)
    bruteforce(li_w, li_sum, l+1, w+li_w[l])

def binsearch(arr, target, start, end):
    while start < end:
        mid = (start + end)//2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return end

bruteforce(li_a, sum_a, 0, 0)
bruteforce(li_b, sum_b, 0, 0)
sum_b.sort()
cnt = 0
for i in sum_a:
    if C-i < 0:
        continue
    cnt += binsearch(sum_b, C-i, 0, len(sum_b))
print(cnt)