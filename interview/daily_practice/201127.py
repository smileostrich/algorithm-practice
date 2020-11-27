# 20.11.27
# merge-sort

li_num = [1,3,2,6,4]

def mergeSort(li):
    if len(li) == 1:
        return li
    l_li = len(li)//2
    g1 = mergeSort(li[:l_li])
    g2 = mergeSort(li[l_li:])

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

print(mergeSort(li_num))