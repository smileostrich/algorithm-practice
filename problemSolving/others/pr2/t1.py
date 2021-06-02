dic_mapper = {'1':['1'],'2':['2'],'3':['3'],'4':['4'],'5':['5'],'6':['6'],'7':['7'],'8':['8'],'9':['9'],'0':['0'],'z':['zero'],'o':['one'],'t':['two','three'],'f':['four','five'],'s':['six','seven'],'e':['eight'],'n':['nine']}
dic_change = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
def solution(s):
    size = len(s)
    result = ''
    idx = 0
    while idx < size:
        cur = dic_mapper[s[idx]]
        if len(cur) == 1:
            if len(cur[0]) == 1:
                result += cur[0]
                idx += 1
            else:
                result += dic_change[cur[0]]
                idx += len(cur[0])
        else:
            for word in cur:
                t_idx = idx
                for w in word:
                    if w != s[t_idx]:
                        break
                    t_idx += 1
                else:
                    idx = t_idx
                    result += dic_change[word]
                    break
    return result

print(solution(	"one4seveneight"))