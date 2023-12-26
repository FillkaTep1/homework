a='туда сюда'#a=4,e=3
a=list(a)
m=[]
for i in range(len(a)):
    if a[i]=='а':
        m.append('4')
    elif a[i]=='т':
        m.append('3')
    else:
        m.append(a[i])
print(''.join(m))