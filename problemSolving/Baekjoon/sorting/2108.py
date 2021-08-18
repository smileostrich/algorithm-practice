import sys
from collections import Counter

N = int(sys.stdin.readline())
li_n = [int(sys.stdin.readline()) for _ in range(N)]
li_n.sort()
print(round(sum(li_n)/len(li_n)))
print(li_n[len(li_n)//2])
cnt_li = Counter(li_n).most_common()
if len(cnt_li) > 1 and cnt_li[0][1] == cnt_li[1][1]:
    print(cnt_li[1][0])
else:
    print(cnt_li[0][0])
print(li_n[-1]-li_n[0])