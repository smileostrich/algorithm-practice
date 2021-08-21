n = int(input())

if n == 0:
    print(0)
elif n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    li_fi = [0,1,1]
    for i in range(3,n+1):
        li_fi.append(li_fi[i-1]+li_fi[i-2])
    print(li_fi[-1])
