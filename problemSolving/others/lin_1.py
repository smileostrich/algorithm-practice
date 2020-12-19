import sys
import math

test = '73425'
res_test = test
flag = 0
ret = []
def ret_plus(n,id):
    res = int(n[:id]) + int(n[id:])
    return str(res)


for i in range(1, len(res_test)//2+2):
    while True:
        if len(res_test) > 1:
            flag += 1
            if len(res_test) > i:
                res_test = ret_plus(res_test, i)
            else:
                if len(res_test) > 1:
                    res_test = test
                    flag = 0
                    break
                res_test = test
                ret.append(flag)
                flag = 0
                break
        else:
            res_test = test
            ret.append(flag)
            flag = 0
            break

print(ret, res_test)