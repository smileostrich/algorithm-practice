# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, C):
    result = []
    dict_result = {}
    company = C.lower()
    for inner_name in S.split(';'):
        tmp = inner_name.split()
        inner_first = ''.join(tmp[0].split('-'))
        inner_last = ''.join(tmp[-1].split('-'))[:8]
        inner_email = (inner_first + '.' + inner_last).lower()
        if inner_email in dict_result:
            dict_result[inner_email] += 1
            # result += ', '+ inner_email + dict_result[inner_email]
            # f', {inner_email}{dict_result[inner_email]}@{company}.com'
            result.append(f'{inner_name} <{inner_email}{dict_result[inner_email]}@{company}.com>')
        else:
            dict_result[inner_email] = 1
            # result += f', {inner_email}@{company}.com'
            result.append(f'{inner_name} <{inner_email}@{company}.com>')
    return ';'.join(result)
        # tmp_result = f'<{inner_email}@{C}.com>'.lower()


print(solution( 'John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker', 'Example'))
