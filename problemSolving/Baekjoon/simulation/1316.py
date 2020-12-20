# 1시간 23분
# 자다일어나서 집중못함 + 잘못된 습관
# from sys import stdin
#
# inp = lambda: stdin.readline().rstrip()
#
# N = int(input())
# result = N
#
# for _ in range(N):
#     word = inp()
#     if len(word) == 1:
#         continue
#     g_check = True
#     for al in set(word):
#         new_word = word
#         while new_word and g_check:
#             tmp = new_word.find(al)
#
#             new_word = new_word[:tmp] + new_word[tmp + 1:]
#             new_tmp = new_word.find(al)
#             if new_tmp == -1:
#                 break
#             elif new_tmp-tmp:
#                 g_check = False
#                 break
#     if not g_check:
#         result -= 1
#
# print(result)

result = 0
for i in range(int(input())):
    word = input()
    print(list(word), sorted(word, key=word.find))
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)
# print('fff'.find('a'))