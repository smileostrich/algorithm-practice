def binarySearch(arr, val):
    first, last = 0, len(arr)-1
    flag = 0
    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == val:
            return True
        elif arr[mid] > val:
            if flag == -1:
                return False
            last = mid-1
            flag = -1
        else:
            if flag == 1:
                return False
            first = mid+1
            flag = 1
    return False

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    li_n = sorted(list(map(int, input().split())))
    li_m = list(map(int, input().split()))
    answer = 0
    for i in li_m:
        if binarySearch(li_n, i):
            answer += 1
    print(f'#{tc} {answer}')