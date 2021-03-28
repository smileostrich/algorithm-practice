T = int(input())

li_N = [int(input()) for _ in range(T)]
dic_stack = {}
high = 0
for i in li_N:
    if i % 2 == 0 and i > high:
        high = i

def recur(L):
    if L == 0:
        return 1
    elif dic_stack[L] >= 0:
        return dic_stack[L]
    else:
        dic_stack[L] = 0
        for i in range(2, high+1, 2):
            dic_stack[L] += recur(i-2) * recur(L-i)
            dic_stack[L] %= 1000000007
        return dic_stack[L]

# for i in range(2, high+1, 2):
recur(high)
print(dic_stack)
#
# dic_stack = {2:['()']}
# dic_count = {2:1}
# for i in range(4, high+1):
#     if i % 2 == 0:
#         li_tmp = []
#         for cur in dic_stack[i - 2]:
#             for k in range(len(cur)+1):
#                 li_tmp.append(cur[:k]+'()'+cur[k:])
#         this = list(set(li_tmp))
#         dic_stack[i] = this
#         dic_count[i] = len(this)
# for i in li_N:
#     if i % 2 == 0:
#         print(dic_count[i]%1000000007)
#     else:
#         print(0)
