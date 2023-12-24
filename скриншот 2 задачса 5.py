def round_standard(num):
    if num >= 0:
        sign = 2
    else:
        sign = -2
    return sign * int((abs(num) + 0.5))
print(round_standard(2))