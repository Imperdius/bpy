state = 1
while True:
    while state == 1:
        print("Insert £1 in 50p or £1 coins")
        coin = input(">").lower()
        if coin != ("50p") and coin != ("£1") and coin != ("50"):
            print("coin rejected")
        else:
            if coin == ("50"):
                print("50 whats? elephants?")
            elif coin == ("50p"):
                state = state + 1
            elif coin == ("£1"):
                state = state + 2
    while state == 2:
        print("Insert 50p")
        coin == input(">").lower()
        if coin != ("50p"):
            print("coin rejected")
        else:
            state = state + 1
    while state == 3:
        print("Printing ticket...")
        print("----------------------------------------")
        state = 1
