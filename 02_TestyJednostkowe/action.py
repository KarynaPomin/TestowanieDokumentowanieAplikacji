def NWD(a, b):
    while a != b:
        if a > b: a = a - b
        if a < b: b = b - a
    return a
