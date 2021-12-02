def solution(arr):
    answer = [arr[0]]
    last = arr[0]
    for i in arr:
        if last != i:
            answer.append(i)
            last = i

    return answer