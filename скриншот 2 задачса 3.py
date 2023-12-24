def mul_to_int(a, b):
    puk = a * b
    if float(puk).is_integer():
        return int(puk)
    return puk
print(mul_to_int(1, 2))
