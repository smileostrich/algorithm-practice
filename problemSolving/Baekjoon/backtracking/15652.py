N, M = map(int, input().split())
arr = [0 for _ in range(M)]

def back(k):
    if k == M:
        for i in arr:
            print(i, end=' ')
        print('')
        return 0
    for i in range(1, N+1):
        if k == 0:
            arr[k] = i
            back(k+1)
        else:
            if arr[k-1] <= i:
                arr[k] = i
                back(k+1)
back(0)