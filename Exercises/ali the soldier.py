import re
import string

consonants = [i for i in string.ascii_lowercase if i not in ['A', 'E', 'I', 'O', 'U', 'Y']]

code = input()

pattern = '\d{2}[' + ''.join(consonants) + ']\d{3}-\d{2}'

if not re.match(pattern, code):
    print("Pattern not found")
    print("invalid")
else:
    two_digits = [code[i] + code[i+1] for i in range(len(code) - 1) \
        if re.match('\d\d', code[i] + code[i+1])] 
    
    print(two_digits)

    flag = "valid"
    for i in two_digits:
        if not int(i[0]) + int(i[1]) % 2 == 0:
            flag = "invalid"
            break 

    print(flag)