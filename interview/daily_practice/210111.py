import math


def binSearch(arr, val,low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if arr[mid] > val:
        return binSearch(arr, val, low, mid-1)
    elif arr[mid] < val:
        return binSearch(arr, val, mid+1, high)
    else:
        return mid


def mergeSort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    g1 = mergeSort(list[:mid])
    g2 = mergeSort(list[mid:])
    result = []
    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result

# def Stupid(arr):
#     n = len(arr)
#     if n==2 and arr[0] > arr[1]:
#         arr[0], arr[1] = arr[1], arr[0]
#         return arr[:n]
#     else:
#         m = math.ceil(2*n//3)
#         result = Stupid(arr[:m])
#         Stupid(result[n-m:])
#         Stupid(result[:m])
#         return result[:n]
#
#
# print(Stupid([3,2,1]))
#
# d = [5, 2, 3, 4, 1]
# print(mergeSort(d))

# arr = [1,1,1,2,2]
# print(binSearch(arr, 2, 0, len(arr)))

result = []
__fibo_cache = {1:1,2:1}
def fibo_recur(n):
    if n in __fibo_cache:
        return __fibo_cache[n]
    else:
        __fibo_cache[n] = fibo_recur(n-2) + fibo_recur(n-1)
        return __fibo_cache[n]

print(fibo_recur(5))

dp_result = {1:1,2:1}
def fibo_dp(n):
    if n <= 2:
        return dp_result[n]
    else:
        for i in range(3, n+1):
            dp_result[i] = dp_result[i-1] + dp_result[i-2]
        return dp_result[n]

print(fibo_dp(7))

def fibo_slide(n):
    if n < 2:
        return n
    v0, v1 = 0, 1
    for _ in range(n-1):
        v0, v1 = v1, v1 + v0
    return v1

print(fibo_slide(7))

