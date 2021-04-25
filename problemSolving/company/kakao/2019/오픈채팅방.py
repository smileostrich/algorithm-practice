def solution(record):
    dic_user = {}
    li_move = []
    for s in record:
        if s[0] == 'E':
            op,uid,name = s.split()
            dic_user[uid] = name
            li_move.append((True,uid))
        elif s[0] == 'L':
            op, uid = s.split()
            li_move.append((False, uid))
        elif s[0] == 'C':
            op, uid, name = s.split()
            dic_user[uid] = name
    result = []
    for o,u in li_move:
        if o:
            result.append(f'{dic_user[u]}님이 들어왔습니다.')
        else:
            result.append(f'{dic_user[u]}님이 나갔습니다.')
    return result

print(solution(	["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))