def solution(s):
    ssize = len(s)
    if ssize <= 2:
        return ssize

    shortest = ssize
    mid = ssize // 2
    for i in range(mid, 0, -1):
        chunks = [s[k:k + i] for k in range(0, ssize, i)]
        end = 0
        if ssize % i != 0:
            end = len(chunks.pop())
        visited = []
        tlist = [1] * len(chunks)
        t_cnt = 0

        chunks.reverse()

        def test(current):
            # if len(chunks) == 0:
            #     return 0
            while chunks:
                neighbor = chunks[-1]
                if neighbor != current:
                    visited.append(neighbor)
                    return 0
                else:
                    chunks.pop()
                    tlist[cnt] += 1

        cnt = 0
        while chunks:
            current = chunks.pop()
            if current not in visited:
                visited.append(current)
                test(current)
            else:
                tlist[cnt] += 1
            cnt += 1

        # 1은 빼기
        for v in tlist:
            if v > 1:
                t_cnt += 1
        tmp = (len(visited) * i) + t_cnt + end
        if shortest > tmp:
            shortest = tmp
    print(shortest)
    return shortest


# data set
solution("aabbaccc")
solution("ababcdcdababcdcd")
solution("abcabcdede")
solution("abcabcabcabcdededededede")
solution("xababcdcdababcdcd")


# for idx in range(0, len(chunks) - 1):
#     ch = chunks[idx]
#     visited.append(ch)
#     for j in range(1, len(chunks)):
#         if chunks[j] != ch:
#             visited.append(chunks[j])
#             break
#         else:
#             tlist[idx] += 1


# test = {}
#
# for k in chunks:
#     if k in test:
#         test[k] += 1
#     else:
#         test[k] = 0
# for v in test.values():
#     if v > 1:
#         t_cnt += 1
# tmp = (len(test) * i) + t_cnt + end