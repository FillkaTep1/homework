a=[1,4,6,7,9]
def g(a):
    v='p'
    for i in range(len(a)-1):
        if a[i]>=a[i+1]:
            v='true'
    if v == 'true':
        return(True)
print(g(a))