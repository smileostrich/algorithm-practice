while True:
    a,b = map(int, input().split())
    if a == b == 0:
        break
    if b % a == 0 and b > a:
        print('factor')
    elif a%b == 0 and a>b:
        print('multiple')
    else:
        print('neither')
