# 다시구현
# import unittest
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less, more, equal = [], [], []
    for each in arr:
        if each < pivot:
            less.append(each)
        elif each > pivot:
            more.append(each)
        else:
            equal.append(each)
    return quick_sort(less) + equal + quick_sort(more)


arr = [6, 5, 1, 4, 7, 2, 3]
print(quick_sort(arr))
# def quick_sort(arr):
#     def sort(low, high):
#         if high <= low:
#             return
#
#         mid = partition(low, high)
#         sort(low, mid - 1)
#         sort(mid, high)
#
#     def partition(low, high):
#         pivot = arr[(low + high) // 2]
#         while low <= high:
#             while arr[low] < pivot:
#                 low += 1
#             while arr[high] > pivot:
#                 high -= 1
#             if low <= high:
#                 arr[low], arr[high] = arr[high], arr[low]
#                 low, high = low + 1, high - 1
#         return low
#
#     return sort(0, len(arr) - 1)
# arr = [6, 5, 1, 4, 7, 2, 3]
# print(quick_sort2(arr))
# print(arr)


# def preprocess_quickSort(list):
#     quickSort(list, 0, len(list)-1)
#     return list
#
#
# def quickSort(list, start, end):
#     if start < end:
#         pivot = partition(list, start, end)
#         quickSort(list, start, pivot-1)
#         quickSort(list, pivot+1, end)
#
#
# def partition(list, start, end):
#     pivot = list[end]
#     wall = start
#     current = start
#
#     for _ in range(start, end):
#         if list[current] <= pivot:
#             list[wall], list[current] = list[current], list[wall]
#             wall += 1
#         current += 1
#     # list[wall], list[current] = list[current], list[wall]
#     list[wall], list[end] = pivot, list[wall]
#     return wall

# 조금 변형버전
# def partition(list, start, end):
#     current = start-1
#     pivot = list[end]
#
#     for comp in range(start, end):
#         if list[comp] <= pivot:
#             current += 1
#             list[current], list[comp] = list[comp], list[current]
#     list[current+1], list[end] = list[end], list[current+1]
#     return current + 1




# use while
# def partition(list, start, end):
#     pivot = end
#     wall = start
#     left = start
#
#     while left < pivot:
#         if list[left] < list[pivot]:
#             list[wall], list[left] = liskjljjt[left], list[wall]
#             wall += 1
#         left += 1
#     list[wall], list[pivot] = list[pivot], list[wall]
#     pivot = wall
#     return pivot


# class unit_test(unittest.TestCase):
#     def test(self):
#         # list = [1, 2, 3, 4, 5, 6, 7]
#         # self.assertEqual([1, 2, 3, 4, 5, 6, 7], preprocess_quickSort(list))
#         list = [8, 13, 2, 6, 1, 4]
#         self.assertEqual([1, 2, 4, 6, 8, 13], preprocess_quickSort(list))
#         list = [8, 1, 2, 5, 10, 14, 7, 21]
#         self.assertEqual([1, 2, 5, 7, 8, 10, 14, 21], preprocess_quickSort(list))

