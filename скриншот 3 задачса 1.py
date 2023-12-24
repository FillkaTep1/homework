def dislike_6(a):
    if (type(a) is float or type(a) is int) and a == 6.0:
        return 'Только не 6!'
    return True
print(dislike_6('отлично'))