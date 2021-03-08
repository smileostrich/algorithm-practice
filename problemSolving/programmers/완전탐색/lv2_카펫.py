# 21분
def solution(brown, yellow):
    answer = []
    if yellow == 1:
        return [3,3]
    for i in range(1, yellow//2+1):
        if yellow % i == 0:
            if (i*2 + (yellow//i+2)*2) == brown:
                answer.append(yellow//i+2)
                answer.append(i+2)
                break
    return answer