s_out = ''


def trim(s):
    global s_out
    if s[0] != ' ' and s[len(s) - 1] == ' ':
        s_out = s[0:len(s) - 1]
    elif s[0] == ' ' and s[len(s) - 1] != ' ':
        s_out = s[1:len(s)]
    elif s[0] == ' ' and s[len(s) - 1] == ' ':
        s_out = s[1:len(s) - 1]
    else:
        pass
    return s_out


s1 = ' abcd '
print(len(s1))
# print(s1[0:3])

print(trim(s1))
