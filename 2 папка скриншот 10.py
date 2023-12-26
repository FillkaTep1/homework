a=input().split()
b=input().split()
def r (a,b):
    c=[]
    l=[]
    for i in range(len(max(a,b))):
        c.append(a[i])
        c.append(b[i])
        l.append(c)
        c=[]
    print(l)
r(a,b)