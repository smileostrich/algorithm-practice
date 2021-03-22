def solution(program, flag_rules, commands):
    result = []
    flag_type = {}

    # flag_type rule
    # 0은 str, 1은 num, 2는 null
    for flag in flag_rules:
        f_name, f_arg = flag.split()
        if f_arg == 'STRING':
            flag_type[f_name] = 0
        elif f_arg == 'STRINGS':
            flag_type[f_name] = 1
        elif f_arg == 'NUMBER':
            flag_type[f_name] = 2
        elif f_arg == 'NUMBERS':
            flag_type[f_name] = 3
        else:
            flag_type[f_name] = 4

    for command in commands:
        tmp = list(command.split())
        size = len(tmp)
        f_keys = flag_type.keys()
        if program != tmp[0]:
            result.append(False)
        else:
            op_idx = 1
            while op_idx < size:
                cur_op = tmp[op_idx]
                # 명령어 존재 여부
                if cur_op in f_keys:
                    # 0일때(str)
                    if flag_type[cur_op] == 0:
                        # weight : 인자의 갯수 대한 인덱스
                        weight = 1
                        # 인자 갯수 찾기 logic
                        while True:
                            if op_idx + weight >= size:
                                weight -= 1
                                break
                            else:
                                if tmp[op_idx + weight][0] == '-':
                                    weight -= 1
                                    break
                                else:
                                    weight += 1
                        # 인자 validation check
                        if weight <= 0:
                            result.append(False)
                            break
                        else:
                            chk_alp = 1
                            for k in range(1, weight+1):
                                if not tmp[op_idx + k].isalpha():
                                    chk_alp = 0
                                    break
                            if chk_alp == 0:
                                result.append(False)
                                break
                    # 1일때(num)
                    elif flag_type[cur_op] == 1:
                        # weight : 인자의 갯수 대한 인덱스
                        weight = 1
                        # 인자 갯수 찾기 logic
                        while True:
                            if op_idx + weight >= size:
                                weight -= 1
                                break
                            else:
                                if tmp[op_idx + weight][0] == '-':
                                    weight -= 1
                                    break
                                else:
                                    weight += 1
                        # 인자 validation check
                        if weight <= 0:
                            result.append(False)
                            break
                        else:
                            chk_alp = 1
                            for k in range(1, weight + 1):
                                if not tmp[op_idx + k].isdigit():
                                    chk_alp = 0
                                    break
                            if chk_alp == 0:
                                result.append(False)
                                break
                    # 2일때(null)
                    else:
                        op_idx += 1
                        continue
                else:
                    result.append(False)
                    break
            else:
                result.append(True)
    return result

print(solution("line", ["-s STRINGS", "-n NUMBERS", "-e NULL"], ["line -n 100 102 -s hi -e", "line -n id pwd -n 100"]))