import collections

N = int(input())
arr = list(map(int, input().split()))
counter = collections.Counter(arr)
if max(counter.values()) > 2 or len(counter.keys()) != max(counter.keys())+1:
    print(0)
else:
    keys = sorted(counter.keys())
    result = 1
    cnt_post = counter[0]
    flag = True
    cnt_one = False
    for i in keys:
        if cnt_post < counter[i]:
            flag = False
            break
        else:
            cnt_post = counter[i]
            if counter[i] == 2:
                result *= 2
            else:
                cnt_one = True
    if flag:
        if cnt_one:
            print(result*2)
        else:    
            print(result)
    else:
        print(0)