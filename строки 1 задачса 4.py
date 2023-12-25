def camel(st):
    new_st = ''
    letter_counter = 0
    for index, val in enumerate(st):
        if val.isalpha():
            if letter_counter % 2 == 0:
                new_st += val.upper()
            else:
                new_st += val.lower()
            letter_counter += 1
        else:
            new_st += val
    return new_st
print(camel('ЕмаЕ Маама ЗвОнИт'))