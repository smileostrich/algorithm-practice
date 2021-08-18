N = int(input())
li_n = list(map(int, input().split()))
dic_r = {val:str(idx) for idx,val in enumerate(sorted(list(set(li_n))))}
result = ''
for i in li_n:
    result += dic_r[i] + ' '
print(result)
