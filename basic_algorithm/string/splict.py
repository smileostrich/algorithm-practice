# def check_strings_re(search_string, input_string):
#     import re
#     return [any(l)
#             for l in
#             zip(*re.findall('|'.join('(' + i + ')' for i in search_string),
#                             input_string))]


def check_strings(search_list, input_string):
    return [s in input_string for s in search_list]


def check_strings_re(search_string, input_string):
    import re
    return [any(l)
            for l in
            zip(*re.findall('|'.join('(' + i + ')' for i in search_string),
                            input_string))]


search_strings = ["hello", "world", "goodbye"]
test_string = "hello world"
assert check_strings(search_strings, test_string) == [True, True, False]
assert check_strings_re(search_strings, test_string) == [True, True, False]