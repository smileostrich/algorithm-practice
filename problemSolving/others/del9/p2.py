from collections import Counter

def solution(research, n, k):
    s_research = list(set(list(''.join(research))))
    s_research.sort()
    dic_word = {i:[0]*len(research) for i in s_research}
    for idx, word in enumerate(research):
        for key,v in Counter(word).most_common():
            dic_word[key][idx] = v
    h_cnt = 0
    result = ''
    for word in s_research:
        cur_cnt = 0
        con = 0
        word_sum = 0
        for idx, cur in enumerate(dic_word[word]):
            if cur >= k:
                word_sum += cur
                con += 1
                if con == n:
                    if 2*n*k <= word_sum:
                        cur_cnt += 1
                    word_sum -= dic_word[word][idx-n+1]
                    con = n-1
            else:
                con = 0
                word_sum = 0
        if cur_cnt > h_cnt:
            h_cnt = cur_cnt
            result = word
    if h_cnt==0:
        return "None"
    else:
        return result


print(solution(["yxxy", "xxyyy", "yz"], 2, 1))