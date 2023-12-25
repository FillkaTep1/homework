def shortener(st):
    while '(' in st or ')' in st:
        left = st.rfind('(')
        right = st.find(')', left)
        st = st.replace(st[left:right + 1], '')
    return st
print(shortener('добрый(лишнее (лишнее) лишнее) вечер ок (лишнее)'))