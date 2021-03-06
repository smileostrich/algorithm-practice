# 재귀
def binarySearch(array, value, low, high):
    if low > high:
        return False
    mid = (low+high) / 2
    if array[mid] > value:
        return binarySearch(array, value, low, mid-1)
    elif array[mid] < value:
        return binarySearch(array, value, mid+1, high)
    else:
        return mid

# 비재귀
def binarySearch2(arr, val):
    first, last = 0, len(arr)-1
    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            last = mid-1
        else:
            first = mid+1
    return -1


print(binarySearch2([1,1,1,2,2],2))
