sen = input()
num = []
li_m = sen.split('-')
result = sum(map(int, li_m[0].split('+')))
if len(li_m) > 1:
    for i in range(1,len(li_m)):
        result -= sum(map(int, li_m[i].split('+')))
print(result)
