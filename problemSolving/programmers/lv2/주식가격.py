def solution(prices):
    li_result = []
    size = len(prices)
    for i in range(0,size-1):
        cnt = 1
        for j in range(i+1, size):
            if prices[i] > prices[j]:
                li_result.append(cnt)
                break
            else:
                cnt += 1
        else:
            li_result.append(size-1-i)
    li_result.append(0)
    return li_result