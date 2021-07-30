from itertools import combinations

n, m = map(int, input().split())
li_cards = list(map(int, input().split()))
hi = 0
for i in combinations(li_cards,3):
    if sum(i) <= m:
        hi = max(hi,sum(i))
print(hi)
