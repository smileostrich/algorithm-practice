import math
# N = int(input())
# li_n = list(map(int, input().split()))

N = 6
li_n = [10, 20, 10, 30, 20, 50]

def lis(arr):
    arr = [-math.inf] + arr
    N = len(arr)
    cache = [-1] * N
    def find(start):
        if cache[start] != -1:
            return cache[start]
        ret = 0
        for nxt in range(start+1, N):
            if arr[start] < arr[nxt]:
                ret = max(ret, find(nxt)+1)
        cache[start] = ret
        return ret
    return find(0)
print(lis(li_n))


# N = int(input())
# li_n = list(map(int, input().split()))

def lis(arr):
    if not arr:
        return 0

    INF = float('inf')
    d = [INF] * (len(arr)+1)
    d[0] = -INF
    d[1] = arr[0]
    answer = 1

    def search(l, r, n):
        if l == r:
            return l
        elif l + 1 == r:
            return l if d[l] >= n else r

        mid = (l + r) // 2
        if d[mid] == n:
            return mid
        elif d[mid] < n:
            return search(mid+1, r, n)
        else:
            return search(l, mid, n)


    for n in arr:
        if d[answer] < n:
            answer += 1
            d[answer] = n
        else:
            next = search(0, answer, n)
            d[next] = n

    return answer
print(lis(li_n))