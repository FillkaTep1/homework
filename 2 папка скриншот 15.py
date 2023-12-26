a='2, 0, 0, 7'
def g (a):
    l=1
    for i in range(len(a)):
        if i %3==0:
            t=int(a[i])
            l=l*t
    return(l)
print(g(a))