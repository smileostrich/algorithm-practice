import math

def calculate(num, idx, add, sub, mul, div):
    global N, high, low
    if idx == N:
        high = max(num, high)
        low = min(num, low)
        return
    else:
        if add:
            calculate(num + li_num[idx], idx+1, add-1, sub, mul, div)
        if sub:
            calculate(num - li_num[idx], idx+1, add, sub-1, mul, div)
        if mul:
            calculate(num * li_num[idx], idx+1, add, sub, mul-1, div)
        if div:
            calculate(int(num / li_num[idx]), idx+1, add, sub, mul, div-1)


N = int(input())
li_num = list(map(int, input().split()))
li_op = list(map(int, input().split()))
# dic_op = {'+':li_op[0], '-':li_op[1], '*':li_op[2], '/':li_op[3]}
high = -10000000000
low = math.inf
calculate(li_num[0],1,li_op[0],li_op[1],li_op[2],li_op[3])
print(high)
print(low)