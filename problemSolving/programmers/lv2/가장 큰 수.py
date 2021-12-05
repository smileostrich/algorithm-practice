def solution(numbers):
    tmp = list(map(str, numbers))
    tmp.sort(key=lambda x:x*3, reverse=True)
    return str(int(''.join(tmp)))