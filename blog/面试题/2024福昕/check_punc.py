
def check(s):
    tmp = []
    for c in s:
        if len(tmp) < 1:
            if c in [')', '}', ']']:
                return False
            tmp.append(c)
        else:
            if tmp[-1] == '(' and c == ')':
                del tmp[-1]
            elif tmp[-1] == '{' and c == '}':
                del tmp[-1]
            elif tmp[-1] == '[' and c == ']':
                del tmp[-1]
    if len(tmp) == 0:
        return True
    return False


s = '([]){}'
s = '([)]'
print(check(s))


