def solution(n):
    number = [1,2,4]
    answer = ''
    while n:
        answer = str(number[(n-1)%3]) + answer
        n = (n-1) // 3
    return answer


# from collections import deque
# def solution(n):
#     result = deque([1])
#     cnt = 0
#     for _ in range(n-1):
#         if cnt == 2:
#             for k in range(len(result)-1,-1,-1):
#                 if result[k] == '1':
#                     result[k] = '2'
#                     break
#                 elif result[k] == '2':
#                     result[k] = '4'
#                     break
#                 else:
#                     if k == 0:
#                         result[k] = '1'
#                         result.appendleft('1')
#                         break
#                     else:
#                         result[k] = '1'
#             cnt = 0
#         else:
#             if cnt == 0:
#                 result[-1] = '2'
#             elif cnt == 1:
#                 result[-1] = '4'
#             cnt += 1
#     for i in range(len(result)):
#         result[i] = str(result[i])
#     return int(''.join(list(result)))
#
# print(solution(5))