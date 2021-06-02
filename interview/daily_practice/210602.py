def binsearch(l,r,arr,target):
    if r >= l:
        mid = l + (r-l)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binsearch(mid+1,r,arr,target)
        else:
            return binsearch(l, mid-1, arr, target)
    else:
        return -1

arr = [2, 3, 4, 10, 40]
x = 10

print(binsearch(0,len(arr)-1,arr,x))


def strtoint(s):
    n = 0
    cnt = 0
    isNeg = False

    if s[0] == '-':
        isNeg = True
        cnt = 1
    while cnt < len(s):
        n = n*10 + ord(s[cnt])-ord('0')
        cnt += 1
    if isNeg:
        n = -n
    return n

print(strtoint('73217'))

def inttostr(i):
    isNeg = False
    s = ''
    if i < 0:
        isNeg = True
    while i > 0:
        s += chr(i%10+ord('0'))
        i //= 10
    if isNeg:
        s += '-'
    return s[::-1]

print(inttostr(123456))


def max_heapify(arr, n, idx):
    largest = idx  # Initialize largest as root
    l = 2 * idx + 1
    r = 2 * idx + 2

    if l < n and arr[idx] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != idx:
        arr[idx], arr[largest] = arr[largest], arr[idx]
        max_heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # build heap
    for i in range(n // 2 - 1, -1, -1):
    # for i in range((n-1) // 2, -1, -1):
        max_heapify(arr, n, i)

    # sorting
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)

# arr = [12, 11, 13, 5, 6, 7]
# arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
arr = [1,2,3,4,5,6,7,8,9,10]
heapSort(arr)
print(arr)

# def maxheap(arr, n, idx):
#     largest = idx
#     l = 2 * idx + 1
#     r = 2 * idx + 2

def minheap(arr,idx,heap_size):
    smallest = idx
    l = idx * 2 + 1
    r = idx * 2 + 2
    if l < heap_size and arr[l] < arr[smallest]:
        smallest = l
    if r < heap_size and arr[r] < arr[smallest]:
        smallest = r
    if idx != smallest:
        arr[idx], arr[smallest] = arr[smallest], arr[idx]
        minheap(arr,smallest,heap_size)

def heapsort(arr):
    size = len(arr)
    for i in range(size//2-1,-1,-1):
        minheap(arr, i, size)
    for i in range(size-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        minheap(arr,0,i)

arr = [10,9,8,7,6,5,4,3,2,1]
heapsort(arr)
print(arr)

## meresort 인덱스 버젼(좀 더 빠름)
def merge_sort(a):
    n = len(a)
    if n <= 1:
        return a
    mid = n // 2
    g1 = merge_sort(a[:mid])
    g2 = merge_sort(a[mid:])
    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            a[ia] = g1[i1]
            i1 += 1
        else:
            a[ia] = g2[i2]
            i2 += 1
        ia += 1
    while i1 < len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1
    return a

print(merge_sort([4,3,2,1]))

import random
def quick_sort(a, start_idx, end_idx):
    if start_idx >= end_idx:
        return 0
    pivot_idx = random.randint(start_idx, end_idx)
    pivot_val = a[pivot_idx]
    a[pivot_idx], a[end_idx] = a[end_idx], a[pivot_idx]
    store_idx = start_idx
    for i in range(start_idx, end_idx):
        if a[i] < pivot_val:
            a[i], a[store_idx] = a[store_idx], a[i]
            store_idx += 1
    a[store_idx], a[end_idx] = a[end_idx], a[store_idx]
    quick_sort(a, start_idx, store_idx - 1)
    quick_sort(a, store_idx + 1, end_idx)

a = [4,3,2,1]
quick_sort(a, 0, len(a)-1)
print(a)