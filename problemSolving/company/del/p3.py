# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    if N == 2:
        return []
    else:
        result = []
        sum = 0
        for i in range(1,N,2):
            if sum + i <= N:
                result.append(i)
                sum += i
            else:
                break
        start = 0
        tmp = N - sum
        if tmp % 2 == 0:
            result[-1] += tmp
        elif tmp > result[-1]:
            result.append(tmp)
        else:
            start = 1
            result[-1] += tmp + 1
        return result[start:]



# def solution(N):
#     if N == 2:
#         return []
#     else:
#         result = [0] * 100
#         sum = 0
#         cnt = 0
#         for i in range(1,N,2):
#             if sum + i <= N:
#                 result[cnt] = i
#                 cnt += 1
#                 sum += i
#             else:
#                 break
#         start = 0
#         r = N - sum
#         if r % 2 == 0:
#             result[cnt-1] += r
#         elif r > result[cnt-1]:
#             result[cnt] = r
#             cnt += 1
#         else:
#             start = 1
#             result[cnt - 1] += r + 1
#         for i in range(start,cnt):
#             print(result[i])


print(solution(39))