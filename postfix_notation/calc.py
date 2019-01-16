def calc(exp):
    array = []
    for i in exp:
        if i.isdigit():
            array.append(int(i))
            continue
        a = array.pop()
        b = array.pop()
        if i == '+':
            res = a + b
        elif i == '-':
            res = a - b
        elif i == '*':
            res = a * b
        elif i == '/':
            res = a // b
        array.append(res)
    return array.pop()
