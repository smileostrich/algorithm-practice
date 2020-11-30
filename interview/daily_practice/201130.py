def heap_sort(arr):
    arr_cp = arr.copy()
    build_min_heap(arr_cp)
    result = []
    print(arr_cp)
    for _ in range(len(arr)):
        arr_cp[0], arr_cp[-1] = arr_cp[-1], arr_cp[0]
        result.append(arr_cp.pop())
        min_heapify(arr_cp, 0)
    return result


def build_min_heap(arr):
    for i in reversed(range((len(arr)-1)//2)):
        min_heapify(arr, i)

def min_heapify(arr, i):
    l = i * 2 + 1
    r = i * 2 + 2
    size = len(arr) - 1
    small_idx = i

    if r <= size and arr[r] < arr[small_idx]:
        small_idx = r
    if l <= size and arr[l] < arr[small_idx]:
        small_idx = l
    if i != small_idx:
        arr[small_idx], arr[i] = arr[i], arr[small_idx]
        min_heapify(arr, small_idx)



arr = [4,5,7,2,3,9]
print(heap_sort(arr))