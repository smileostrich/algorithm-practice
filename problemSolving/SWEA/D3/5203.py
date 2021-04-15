from collections import Counter


def is_triplet(arr):
    if Counter(arr).most_common()[0][1] >= 3:
        return True
    return False

def is_run(arr):
    for i in range(0,len(arr)-2):
        if arr[i]+2 == arr[i+1]+1 == arr[i+2]:
            return True
    return False

T = int(input())
for tc in range(1, T+1):
    li_load = list(map(int, input().split()))
    li_p1 = []
    li_p2 = []
    for idx, i in enumerate(li_load):
        if idx % 2 == 0:
            li_p1.append(i)
        else:
            li_p2.append(i)
    p1 = p2 = len(li_p1)+10
    for i in range(3,len(li_p1)+1):
        li_t1 = li_p1[:i]
        if is_triplet(li_t1) or is_run(sorted(set(li_t1))):
            p1 = i
            break
    for i in range(3,len(li_p2)+1):
        li_t2 = li_p2[:i]
        if is_triplet(li_t2) or is_run(sorted(set(li_t2))):
            p2 = i
            break
    if p1 == p2:
        if p1 == len(li_p1)+10:
            print(f'#{tc} 0')
        else:
            print(f'#{tc} 1')
    elif p1 < p2:
        print(f'#{tc} 1')
    elif p1 > p2:
        print(f'#{tc} 2')
