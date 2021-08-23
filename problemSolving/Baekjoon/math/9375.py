import math
from collections import defaultdict


T = int(input())
for _ in range(T):
    N = int(input())
    dic_item = defaultdict(list)
    for _ in range(N):
        item, type = input().split()
        dic_item[type].append(item)
    ans = 1
    for i in dic_item.values():
        ans *= len(i)+1
    print(ans-1)