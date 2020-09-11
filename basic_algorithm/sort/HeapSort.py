# using heapq module
import heapq


def min_heapsort(array):
    h = array.copy()
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]


def max_heapsort(array):
    h = []
    for i in array:
        heapq.heappush(h, (-i, i))
    return [heapq.heappop(h)[1] for _ in range(len(h))]

print(min_heapsort([3,7,6,5,4]))
print(max_heapsort([3,7,6,5,4]))

# way 2
# def heapsort(array):
#     array = array.copy()
#     build_min_heap(array)
#     sorted_array = []
#     for _ in range(len(array)):
#         array[0], array[-1] = array[-1], array[0]
#         sorted_array.append(array.pop())
#         min_heapify(array, 0)
#     return sorted_array
#
#
# def build_min_heap(array):
#     for i in reversed(range(len(array)//2)):
#         min_heapify(array, i)
#
#
# def min_heapify(array, i):
#     left = 2 * i + 1
#     right = 2 * i + 2
#     length = len(array) - 1
#     smallest = i
#     if left <= length and array[i] > array[left]:
#         smallest = left
#     if right <= length and array[smallest] > array[right]:
#         smallest = right
#     if smallest != i:
#         array[i], array[smallest] = array[smallest], array[i]
#         min_heapify(array, smallest)



# way 3
# def heapsort(a):
#     def swap(a,i,j):
#         a[i], a[j] = a[j], a[i]
#
#     def siftdown(a, i, size):
#         l = 2*i+1
#         r = 2*i+2
#         largest = i
#         if l <= size-1 and a[l] > a[i]:
#             largest = l
#         if r <= size-1 and a[r] > a[largest]:
#             largest = r
#         if largest != i:
#             swap(a, i, largest)
#             siftdown(a, largest, size)
#
#     def heapify(a, size):
#         p = (size//2)-1
#         while p >= 0:
#             siftdown(a, p, size)
#             p -= 1
#
#     size = len(a)
#     heapify(a, size)
#     end = size-1
#     while(end > 0):
#         swap(a, 0, end)
#         siftdown(a, 0, end)
#         end -= 1
#
# arr = [1,3,2,4,9,7]
# heapsort(arr)
# print(arr)