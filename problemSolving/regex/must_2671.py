# fullmatch 써야함 fullmatch 몰라서 못품 다시풀어봐야함

import re

signal = input()
test = re.fullmatch(r'((100+1+)+|(01))+', signal)

if test:
    print("SUBMARINE")
else:
    print("NOISE")