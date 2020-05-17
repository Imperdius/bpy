while True:
    check = False
    while check == False:
        i = input(">")
        try:
            float(i)
        except ValueError:
            print("3rhgvjbkcip")
        else:
            check = True
    i = float(i)
    if i % 1 == 0:
        print("integer")
    else:
        print("real")
