# 배열돌리기 익숙해지기
zip()

def roatated(array):
    test = list(zip(*reversed(array)))
    return [list(elem) for elem in test]