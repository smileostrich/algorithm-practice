
boxes = [[1, 2], [2, 3], [3, 1]]
dict_product = {}
size = len(boxes)
cnt = 0
for a, b in boxes:
    if a in dict_product.keys():
        dict_product[a] += 1
    else:
        dict_product[a] = 1
    if b in dict_product.keys():
        dict_product[b] += 1
    else:
        dict_product[b] = 1

for i in dict_product.values():
    if i % 2 == 1:
        cnt += 1

if cnt % 2 == 0:
    print(cnt//2)
else:
    print(cnt//2 + 1)