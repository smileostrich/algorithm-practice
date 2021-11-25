# import string
#
# def toprime(k):
#     t_li_primes = [False, False] + [True] * k
#     for i in range(2, int(k ** 0.5) + 1):
#         if t_li_primes[i]:
#             for j in range(2 * i, k + 1, i):
#                 t_li_primes[j] = False
#     return t_li_primes[k]
#
#
# def is_prime_number(x):
#     for i in range(2, int(x**1/2) + 1):
#         if x % i == 0:
#             return False
#     return True
# print(is_prime_number(2))
#
# def convert(num, base):
#     tmp = string.digits + string.ascii_lowercase
#     q, r = divmod(num, base)
#     if q == 0:
#         return tmp[r]
#     else:
#         return convert(q, base) + tmp[r]
#
# def solution(n, k):
#     p = 10000000
#     li_primes = [False, False] + [True] * p
#     for i in range(2, int(p ** 0.5) + 1):
#         if li_primes[i]:
#             for j in range(2 * i, p + 1, i):
#                 li_primes[j] = False
#     if n == 10:
#         s_con = str(n)
#     else:
#         s_con = convert(n,k)
#     result = 0
#     if s_con.count('0') == 0 and s_con[0] != 0:
#         if int(s_con) < len(li_primes):
#             if li_primes[int(s_con)]:
#                 result += 1
#         else:
#             # if toprime(int(s_con)):
#             result += 1
#     else:
#         for i in s_con.split('0'):
#             if i and i[0] != 0:
#                 i = int(i)
#                 if i < len(li_primes):
#                     if li_primes[i]:
#                         result += 1
#                 else:
#                     # if toprime(int(i)):
#                     result += 1
#     return result


print(solution(	437674, 3))
# print(solution(110011, 10))





















import string

def toprime(x):
    for i in range(2, int(x**1/2) + 1):
        if x % i == 0:
            return False
    return True

def convert(num, base):
    tmp = string.digits + string.ascii_lowercase
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]

def solution(n, k):
    p = 10000000
    li_primes = [False, False] + [True] * p
    for i in range(2, int(p ** 0.5) + 1):
        if li_primes[i]:
            for j in range(2 * i, p + 1, i):
                li_primes[j] = False
    if n == 10:
        s_con = str(n)
    else:
        s_con = convert(n,k)
    result = 0
    if s_con.count('0') == 0 and s_con[0] != 0:
        if int(s_con) < len(li_primes):
            if li_primes[int(s_con)]:
                result += 1
        else:
            if toprime(int(s_con)):
                result += 1
    else:
        for i in s_con.split('0'):
            if i and i[0] != 0:
                i = int(i)
                if i < len(li_primes):
                    if li_primes[i]:
                        result += 1
                else:
                    if toprime(int(i)):
                        result += 1
    return result