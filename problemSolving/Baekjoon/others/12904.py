from collections import deque

s = input()
size = len(s)
tar = input()
queue = deque([tar])
while queue:
    cur = queue.popleft()
    if len(cur) == size and cur == s:
        print(1)
        break
    elif len(cur) > size:
        if cur[-1] == 'A':
            queue.append(cur[0:-1])
        else:
            queue.append(cur[0:-1][::-1])
else:
    print(0)

# from collections import deque
#
# s = input()
# tar = input()
# size = len(tar)
# queue = deque([s])
# while queue:
#     cur = queue.popleft()
#     if len(cur) < size:
#         tmp1 = cur + 'A'
#         tmp2 = cur[::-1] + 'B'
#         if len(tmp1) == size:
#             if tmp1 == tar:
#                 print(1)
#                 break
#         if len(tmp2) == size:
#             if tmp2 == tar:
#                 print(1)
#                 break
# else:
#     print(0)



# from collections import deque
#
# s = list(input())
# tar = list(input())
# queue = deque([list(s)])
# while queue:
#     cur = queue.popleft()
#     if cur == tar:
#         print(1)
#         break
#     elif len(cur) < len(tar):
#         queue.append(cur + ['A'])
#         queue.append(sorted(cur, reverse=True) + ['B'])
# else:
#     print(0)