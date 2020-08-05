# 50분
# import sys
#
# list = [111, 123, 135, 147, 159, 210, 222, 234, 246, 258, 321, 333, 345, 357, 369, 420, 432, 444, 456, 468, 531, 543, 555, 567, 579, 630, 642, 654, 666, 678, 741, 753, 765, 777, 789, 840, 852, 864, 876, 888, 951, 963, 975, 987, 999]
# n = int(sys.stdin.readline())
# k = 111
#
# if n < 100:
#     print(n)
# elif n < 111:
#     print(99)
# elif (n == 1000) or (n == 999):
#     print(144)
# else:
#     for i in range(len(list)):
#         if n >= list[i]:
#             continue
#         else:
#             print(99 + i)
#             break

#아래 소스는 인터넷 참조(이게 내 소스보다 잘짜서 위에 주석처리)
num = int(input())
hansu = 0

for n in range(1, num + 1):
    if n <= 99:  # 1부터 99까지는 모두 한수
        hansu += 1

    else:
        nums = list(map(int, str(n)))  # 숫자를 자릿수대로 분리
        if nums[0] - nums[1] == nums[1] - nums[2]:  # 등차수열 확인
            hansu += 1
print(hansu)