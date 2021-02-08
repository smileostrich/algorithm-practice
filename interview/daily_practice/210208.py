def bubble(li):
    for i in range(len(li)-1, 0, -1):
        for j in range(0, i):
            if li[j] < li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]

li = [3,2,1,6,4]
bubble(li)
print(li)