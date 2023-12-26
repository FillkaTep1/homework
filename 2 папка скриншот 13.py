a = 'бошки дымятся'


def g(a):
    a = list(a)
    a.append('')
    i = 1
    cnd = 1
    m = []
    while cnd != len(a):
        if a[i-1] != ' ' or a[i] != ' ':
            i += 1
            m.append(a[i-1])
        else:
            a.pop(i-1)

        cnd += 1
    
    m.pop(-1)
    return(''.join(m))
print(g(a))