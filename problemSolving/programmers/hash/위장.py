def solution(clothes):
    cl_dict = dict()
    for _ , categori in clothes:
        if categori in cl_dict:
            cl_dict[categori] += 1
        else:
            cl_dict[categori] = 2
    answer = 1
    for cate in cl_dict:
        answer *= cl_dict[cate]
    return answer - 1