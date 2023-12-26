a='шалаш'
def h(a):
    a=a[::-1]
    j=''
    for i in range(len(a)):
        if a[i]==a[i].upper():
            k=a[i].lower()
        if a[i]==a[i].lower():
            k=a[i].upper()
        j+=k
        
        
    print(j)
h(a)