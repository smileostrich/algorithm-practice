# def mergeSort(list):
#     print("Splitting ",list)
#     if len(list) > 1:
#         mid = len(list)//2
#         lefthalf = list[:mid]
#         righthalf = list[mid:]
#
#         mergeSort(lefthalf)
#         mergeSort(righthalf)
#
#         i=0
#         j=0
#         k=0
#         while i < len(lefthalf) and j < len(righthalf):
#             if lefthalf[i] < righthalf[j]:
#                 list[k] = lefthalf[i]
#                 i += 1
#             else:
#                 list[k] = righthalf[j]
#                 j += 1
#             k += 1
#
#         while i < len(lefthalf):
#             list[k] = lefthalf[i]
#             i += 1
#             k += 1
#
#         while j < len(righthalf):
#             list[k] = righthalf[j]
#             j += 1
#             k += 1
#     print("Merging ",list)
#
# list = [6,2,4,1,3,7,5,8]
# mergeSort(list)
# print(list)


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

d = [6, 8, 3, 9, 10, 1, 2, 4, 7]
print(mergeSort(d))
