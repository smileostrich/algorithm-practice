# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def solution(S):
    result = math.inf
    result_s = ''
    li_files = S.split('\n')
    for file in li_files:
        info_file = file.split()
        if info_file[-1][-1] == '~':
            if info_file[0][-1] == 'K':
                flag = True
            elif info_file[0][-1] == 'M':
                if int(info_file[0][:-1]) < 14:
                    flag = True
                else:
                    flag = False
            elif info_file[0][-1] == 'G':
                flag = False
            else:
                flag = True
            if flag:
                li_date = info_file[1].split('-')
                if int(li_date[0]) > 1990:
                    second_flag = True
                elif int(li_date[0]) == 1990:
                    if li_date[1] != '01':
                        second_flag = True
                    else:
                        second_flag = False
                else:
                    second_flag = False
                if second_flag:
                    t_result = info_file[-1].rfind('.')
                    if result > t_result:
                        result = t_result
                        result_s = info_file[-1][:t_result]
    if result_s:
        return str(result)
    else:
        return 'NO FILES'






print(solution(' 715K 2009-09-23 system.zip~\n 179K 2013-08-14 to-do-list.xml~\n 645K 2013-06-19 blockbuster.mpeg~\n  536 2010-12-12 notes.html\n 688M 1990-02-11 delete-this.zip~\n  23K 1987-05-24 setup.png~\n 616M 1965-06-06 important.html\n  14M 1992-05-31 crucial-module.java~\n 192K 1990-01-31 very-long-filename.dll~'))