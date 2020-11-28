# def mergeSort(list):
#     if len(list) == 1:
#         return list
#
#     mid = len(list) // 2
#     g1 = mergeSort(list[:mid])
#     g2 = mergeSort(list[mid:])
#
#     result = []
#     while g1 and g2:
#         if g1[0] < g2[0]:
#             result.append(g1.pop(0))
#         else:
#             result.append(g2.pop(0))
#     while g1:
#         result.append(g1.pop(0))
#     while g2:
#         result.append(g2.pop(0))
#     return result
#



def pre_qucik(list):
    quick_sort(list, 0, len(list)-1)
    return list


def quick_sort(list, start, end):
    if start < end:
        pivot = partition(list, start, end)
        quick_sort(list, start, pivot-1)
        quick_sort(list, pivot+1, end)


def partition(list, start, end):
    current = start-1
    pivot = list[end]

    for comp in range(start, end):
        if list[comp] <= pivot:
            current += 1
            list[current], list[comp] = list[comp], list[current]
    list[current+1], list[end] = list[end], list[current+1]
    return current + 1


# def partition(list, start, end):
#     wall = start
#     current = start
#     pivot = list[end]
#
#     for _ in range(start, end):
#         if list[current] <= pivot:
#             list[current], list[wall] = list[wall], list[current]
#             wall += 1
#         current += 1
#     list[current], list[wall] = list[wall], list[current]
#     return wall



list= [7,4,3,5,6,8,9]
# print(mergeSort([1,4,2,3,7,9]))
print(pre_qucik(list))