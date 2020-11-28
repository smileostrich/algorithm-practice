def pre_quick(list):
    quickSort(list, 0, len(list)-1)
    return list


def quickSort(list, start, end):
    if start < end:
        pivot = partition(list, start, end)
        quickSort(list, start, pivot-1)
        quickSort(list, pivot+1, end)


def partition(list, start, end):
    current = start
    wall = start
    pivot = list[end]

    for _ in range(start, end):
        if list[current] <= pivot:
            list[current], list[wall] = list[wall], list[current]
            wall += 1
        current += 1
    list[current], list[wall] = list[wall], list[current]
    return wall


def merge(list):
    print(list)
    if len(list) <= 1:
        return list

    mid = len(list) // 2
    g1 = merge(list[:mid])
    g2 = merge(list[mid:])

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


############
list = [3,5,2,1,7,0,4,9]

# merge 리스트 새로 만듬
print(merge(list))
# 원래 리스트속
print(pre_quick(list))
