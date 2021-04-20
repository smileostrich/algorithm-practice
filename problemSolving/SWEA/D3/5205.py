def preprocess_quickSort(list):
    quickSort(list, 0, len(list)-1)
    return list


def quickSort(list, start, end):
    if start < end:
        pivot = partition(list, start, end)
        quickSort(list, start, pivot-1)
        quickSort(list, pivot+1, end)


def partition(list, start, end):
    pivot = list[end]
    wall = start
    current = start

    for _ in range(start, end):
        if list[current] <= pivot:
            list[wall], list[current] = list[current], list[wall]
            wall += 1
        current += 1
    list[wall], list[end] = pivot, list[wall]
    return wall


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    li_n = list(map(int, input().split()))
    answer = 0
    li_re = preprocess_quickSort(li_n)
    print(f'#{tc} {li_re[N//2]}')