def build_minheap(li):
    for i in reversed(range(len(li)//2)):
        min_heapify(li, i)

def min_heapify(li, i):
    size = len(li)-1
    r = i*2 +2
    l = i*2 +1
    smallest = i
    if r <= size and li[smallest] > li[r]:
        smallest = r
    if l <= size and li[smallest] > li[l]:
        smallest = l
    if smallest != i:
        li[smallest], li[i] = li[i], li[smallest]
        min_heapify(li, smallest)

def heapsort(li):
    cp_li = li.copy()
    build_minheap(cp_li)
    result = []
    for _ in range(len(cp_li)):
        cp_li[0], cp_li[-1] = cp_li[-1], cp_li[0]
        result.append(cp_li.pop())
        min_heapify(cp_li, 0)
    return result


def pre_qucick(li):
    quick_sort(li, 0, len(li)-1)
    return li

def quick_sort(li, s, e):
    if s < e:
        pivot = partition(li,s,e)
        quick_sort(li, s, pivot-1)
        quick_sort(li, pivot+1, e)

def partition(li, s, e):
    wall = s
    pivot = li[e]

    for i in range(s, e):
        if li[i] < pivot:
            li[wall], li[i] = li[i], li[wall]
            wall += 1
    li[e], li[wall] = li[wall], li[e]
    return wall


li = [3,2,6,1,9]
# print(heapsort(li))
print(pre_qucick(li))
