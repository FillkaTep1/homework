def change(lst):
    matvey_mmm = lst.pop()  
    ne_matvey_mmm = lst.pop(0) 
    lst.append(ne_matvey_mmm) 
    lst.insert(0, matvey_mmm) 
    return lst
print(change([6, 3, 2, 9, 5000000]))