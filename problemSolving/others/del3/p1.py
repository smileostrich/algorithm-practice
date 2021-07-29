from collections import deque

def braces(values):
    for braces in values:
        # li_tmp = deque(list(braces))
        li_result = []
        for brace in braces:
            if brace == '[':
                li_result.append(brace)
            elif brace == '{':
                li_result.append(brace)
            elif brace == ']':
                tmp_brace = li_result.pop()
                if tmp_brace != '[':
                    return 'NO'
            elif brace == '}':
                tmp_brace = li_result.pop()
                if tmp_brace != '{':
                    return 'NO'
        if li_result:
            return 'NO'
        else:
            return 'YES'



print(braces(['{}[]()', '{[}]']))