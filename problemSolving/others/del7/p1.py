from collections import defaultdict

def test(name_list):
    li_alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    dic_name = defaultdict(int)
    li_result = []
    for i in name_list:
        li_result.append(i+li_alpha[dic_name[i]])
        dic_name[i] += 1
    return li_result

print(test(['김비바','김비바','이비바','김토스','이비바','김비바']))