from collections import deque
import math

smallest = math.inf
li_target = []

def process(li, cnt, k):
    global smallest, li_target
    if smallest > cnt:
        if li_target == li:
            smallest = cnt
            return
        size = len(li)
        for i in range(size):
            if i + 1 < size:
                for j in range(i+1,size):
                    if j-i <= k:
                        if li[i] > li[j]:
                            li[i], li[j] = li[j], li[i]
                            process(li, cnt+1, k)
                            li[i], li[j] = li[j], li[i]

def solution(arr, k):
    global li_target
    li_target = sorted(arr)
    process(arr,0,k)
    return smallest


print(solution([4, 5, 2, 3, 1], 4))