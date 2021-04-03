def test(m, k):
    result = m
    tmp = 0
    for i in k:
        if tmp == 0:
            left_str = ''
            right_str = result
        else:
            left_str = result[:tmp]
            right_str = result[tmp:]
        idx = right_str.find(i)
        if idx > 0:
            result = left_str + right_str[0:idx]+right_str[idx+1:]
            tmp = idx
        else:
            result = left_str + right_str[idx+1:]
            tmp = idx
    return result


print(test('acbbcdc', 'abc'))
print(test('kkaxbycyz', 'abc'))