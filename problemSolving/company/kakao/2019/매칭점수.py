import re

def solution(word, pages):
    parser_meta = re.compile(r'<meta(.+)/>')
    parser_content = re.compile('content=\"(.+)\"')
    parser_a = re.compile('<a href="(.+?)\">')
    parser_word = re.compile(word.lower())

    dic_basiclink = dict()
    dic_externallink = dict()
    li_result = []
    for idx, page in enumerate(pages):
        tmp = parser_content.search(parser_meta.search(page).group()).group()[9:-1]
        a_url = parser_a.findall(page)
        cnt = 0
        for i in re.findall('<body>(.+?)</body>', page, re.I|re.S)[0].split():
            for tar in re.split(r'[^A-Za-z]', i):
                word = word.lower()
                if word == tar.lower():
                    cnt += 1
        dic_basiclink[tmp] = [cnt, idx]
        dic_externallink[tmp] = a_url
        li_result.append([cnt, idx])
    for link, val_link in dic_externallink.items():
        for i in val_link:
            if i in dic_basiclink:
                dic_basiclink[i][0] += dic_basiclink[link][0] // len(val_link)

    return sorted(dic_basiclink.values(), key= lambda x: (-x[0], x[1]))[0][1]


print(solution(	"Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))
