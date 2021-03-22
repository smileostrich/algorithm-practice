def solution(program, flag_rules, commands):
    result = []
    flag_type = {}

    # flag_type rule
    # 0은 str, 1은 strs, 2는 num 3은 nums 4는 null
    li_al = []
    for f in len(flag_rules):
        tmp_f = list(flag_rules[f].split())
        if len(tmp_f) >= 3:
            li_al.append(tmp_f)
            continue
        f_name, f_arg = tmp_f
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
    for i in li_al:
        f_name, f_alias, f_name = i.split()
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
                    # null일때
                    if flag_type[cur_op] == 4:
                        op_idx += 1
                        continue
                    # 1,2,3,4 (str, strs, num, nums 일때)
                    else:
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
                            # case string / strings
                            if flag_type[cur_op] == 0:
                                if op_idx + 1 < size:
                                    if tmp[op_idx + 1].isalpha():
                                        op_idx += 2
                                        continue
                                    else:
                                        result.append(False)
                                        break
                                else:
                                    result.append(False)
                                    break
                            elif flag_type[cur_op] == 1:
                                chk_alp = 1
                                for k in range(1, weight + 1):
                                    if not tmp[op_idx + k].isalpha():
                                        chk_alp = 0
                                        break
                                else:
                                    op_idx += weight +1
                                if chk_alp == 0:
                                    result.append(False)
                                    break
                            # case number / numbers
                            elif flag_type[cur_op] == 2:
                                if op_idx + 1 < size:
                                    if tmp[op_idx + 1].isdigit():
                                        op_idx += 2
                                        continue
                                    else:
                                        result.append(False)
                                        break
                                else:
                                    result.append(False)
                                    break
                            elif flag_type[cur_op] == 3:
                                chk_dig = 1
                                for k in range(1, weight + 1):
                                    if not tmp[op_idx + k].isdigit():
                                        chk_dig = 0
                                        break
                                else:
                                    op_idx += weight +1
                                if chk_dig == 0:
                                    result.append(False)
                                    break
                else:
                    result.append(False)
                    break
            else:
                result.append(True)
    return result

print(solution("line", ["-s STRINGS", "-n NUMBERS", "-e NULL"], ["line -n 100 102 -s hi -e", "line -n id pwd -n 100"]))