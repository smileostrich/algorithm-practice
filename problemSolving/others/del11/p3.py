def test(s):
    li_fir = s.split('\"')
    response, bytes = li_fir[-1].split()
    print(li_fir)
    if response == "200":
        status, dir, http = li_fir[-2].split()
        if status == "GET":
            files = dir.split('/')
            if files[-1]:
                result = files[-1]
    return result


print(test("unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] \"GET /images/KSC-logosmall.gif HTTP/1.0\" 200 1204"))