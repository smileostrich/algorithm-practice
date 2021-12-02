def solution(arr, divisor):
    result = []
    for i in arr:
        if i%divisor == 0:
            result.append(i)
    if result:
        result.sort()
        return result
    return [-1]