# internet code
N = int(input())
li_road = list(map(int, input().split()))
li_cost = list(map(int, input().split()))
res = 0
cur_cost = li_cost[0]
for i in range(N-1):
    if li_cost[i] < cur_cost:
        cur_cost = li_cost[i]
    res += cur_cost*li_road[i]
print(res)



# my code
# N = int(input())
# li_road = list(map(int, input().split()))
# li_tmp = list(map(int, input().split()))
# li_oil = [(idx,i) for idx,i in enumerate(li_tmp)]
# li_oil.sort(key=lambda x:(x[1],-x[0]))
# result = 0
#
# r = len(li_road)
# for dis, price in li_oil:
#     if r > dis:
#         result += price*sum(li_road[dis:r])
#         r = dis
# print(result)