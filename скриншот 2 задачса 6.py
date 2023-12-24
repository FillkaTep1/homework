def eqv(a, b, c):
    zov = a + b
    z = 0.01 / 100  
    v = z * max(abs(a), abs(b))  
    return abs(zov - c) <= v  
print(eqv(0.21, 0.35, 0.48))