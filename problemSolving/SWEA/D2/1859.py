import heapq
# T = int(input())

for test_case in range(1, 1 + 1):
    test = [3,4,5]
    heapq.heapify(test)
    for i in test:
        print(heapq.heappop(test))
# import heapq
# T = int(input())
#
# for _ in range(1, T + 1):
#     N = int(input())
#     li_price = list(map(int, input().split()))
#     # h_p = -1
#     heapq.heapify(li_price)
#     h_p = max(li_price)
#     sorted_price = sorted(li_price, reverse=True)
#     heapq.h
#     for idx, price in enumerate(li_price):
#         if price > h_p:
#             h_p = price
#
#     for p in li_price:
#         for c_p in sorted_price:
#             if p >= cp:

