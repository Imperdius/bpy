while True:
    f1 = 0
    f2 = 1
    total = 1
    check = False
    while check == False:
        print("How many fibonacci numbers would you like to count?")
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
    print("Number  1  in the fibbonacci sequence is  1")
    print("Current total: ", total)
    for i in range(count):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        total = total + f3
        print("Number ", i + 2, " in the fibbonacci sequence is ", f3)
        print("Current total: ", total)
        i = i + 1
