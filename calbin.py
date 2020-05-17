def addmenu():
    check = False
    while check == False:
        print("Please enter first number in binary")
        binary = input(">")
        try:
            int(binary, 2)
        except ValueError:
            print("Please only use '1' and '0'")
        else:
            binary = int(binary, 2)
            print("Please enter the second number in binary")
            binary2 = input(">")
            try:
                int(binary2, 2)
            except ValueError:
                print("Please only use '1' and '0'")
            else:
                binary2 = int(binary2, 2)
                btotal = str(bin(binary + binary2))
                print(btotal[2:])
                check = True

def convmenu():
    check = False
    while check == False:
        print("Please enter number in binary")
        binary = input(">")
        try:
            int(binary, 2)
        except ValueError:
            print("You are a fool, a buffoon, and a stupid member of the land")
            print("Please only use '1' and '0'")
        else:
            binary = int(binary, 2)
            print(chr(binary))
            check = True


if __name__ == "__main__":
    check = False
    while check == False:
        print("Would you like to add binary or convert binary to ascii?")
        print("1) Add")
        print("2) Convert")
        mchoice = input(">")
        try:
            int(mchoice)
        except ValueError:
            print("Please enter one of the options")
        else:
            if mchoice == "1":
                addmenu()
            elif mchoice == "2":
                covmenu()
            else:
                print("Please enter one of the options")
