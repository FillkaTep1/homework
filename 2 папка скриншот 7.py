a='забирай меня скорей'
def g(a):
    m=[]
    for i in range(len(a)):
        h=ord(a[i])-96
        m.append(h)
    print(m)
g(a)