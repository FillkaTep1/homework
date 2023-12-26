a=[1,4,3,2]
def b(a):
    h=0
    m=[]
    for i in range(len(a)):
        t=a[i]
        h+=t
        m.append(h)
    print(m)
b(a)