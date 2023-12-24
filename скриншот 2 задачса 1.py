def to_float(num):
    if isinstance(num, (int, float)):
        return float(num)
    return "Нельзя преобразовать"
print(to_float("додж_челенджер"))