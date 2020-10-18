# re 32분
# 이 소스 시간초과 뜸 -> 그냥 팀소트(내장 소트 함수) 사용 해야하는듯
# import sys
#
#
# N = int(sys.stdin.readline().rstrip())
# nList = [int(sys.stdin.readline().rstrip()) for i in range(N)]
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
#         if pivot > nList[current]:
#             nList[wall], nList[current] = nList[current], nList[wall]
#             wall += 1
#         current += 1
#     nList[wall], nList[current] = pivot, nList[wall]
#     return wall
#
#
# quickSort(nList, 0, len(nList)-1)
# for i in nList:
#     print(i)

def mergeSort(list):
    if len(list) < 2:
        return list
    mid = len(list)//2
    g1 = mergeSort(list[:mid])
    g2 = mergeSort(list[mid:])
    result = []

    while g1 and g2:
        if g1[0] > g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result
