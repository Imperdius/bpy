while True:
    f1 = 0
    f2 = 1
    total = 1
    check = False
    while check == False:
        print("Enter hack key")
        count = input(">")
        try:
            int(count)
        except ValueError:
            print("Please enter a number")
        else:
            check = True
    count = int(count)
    i = 0
    i = i + 1
    count = count - 1
    print("Warming up hack")
    print("Current total: ", total)
    for i in range(count):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        f3 = 2^f3
        total = total + f3
        print( i + 2, f3)
        print(total)
        i = i + 1
