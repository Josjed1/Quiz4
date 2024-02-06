def ambiguous(x, y):
    print()
    print("From Function3:")
    if (type(x) == str and type(y) == str) or (type(x) == int and type(y) == int):
        print(str(x) + str(y))
        print(str(y) + str(x))
    elif type(x) == str and type(y) == int:
        z = str(y)
        print(x + z)
        print(z + x)
    elif type(x) == int and type(y) == str:
        z = str(x)
        print(z + y)
        print(y + z)