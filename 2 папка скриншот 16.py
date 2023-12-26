a=[[1,2,3],[4,5,6],[7,8,9]]

def v(a):
    v=0
    for i in range(len(a)):
        v+=(a[i][0]*a[i][1]*a[i][2])
    print(v)
v(a)