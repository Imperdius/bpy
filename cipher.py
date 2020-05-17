import random
global text = ""
global key = ""

while True:

    def printOptions():
        check = False
        while check == False:
            print("Select a menu")
            print("1) Text/Key")
            print("2) Encrypt/Decrypt")
            choice = input(">")
            try:
                int(choice)
            except ValueError:
                print("Please enter one of the options")
            else:
                if int(choice) > 2 or int(choice) < 1:
                    print("Please enter one of the options")
                else:
                    return(int(choice))

    def textMenu():
        check = False
        while check == False:
            print("Select an option")
            print("1) View text")
            print("2) Set text")
            print("3) Clear text")
            print("4) Set key")
            print("5) Clear key")
            choice = input(">")
            try:
                int(choice)
            except ValueError:
                print("Please enter one of the options")
            else:
                if int(choice) > 5 or int(choice) < 1:
                    print("Please enter one of the options")
                else:
                    return(int(choice))

    def cryptMenu():
        check = False
        while check == False:
            print("Select an otion")
            print("1) Encrypt")
            print("2) Decrypt")
            choice = input(">")
            try:
                int(choice)
            except ValueError:
                print("Please enter one of the options")
            else:
                if int(choice) > 2 or int(choice) < 1:
                    print("Please enter one of the options")
                else:
                    return(int(choice))

    def show(o):
        if o == "text":
            print(text)
        elif o == "key":
            print(key)

    def modify(op, var):
        if op == "set":
            if var == "text":
                print("What would you like to set the text to?")
                text = input(">")
            if var == "key":
                check = False
                while check == False:
                    print("What would you like to set the key input to? (Your actual key will be different)")
                    print("Enter any number, or 'r' for a random key")
                    inp = input(">")
                    if inp == "r":
                        check = True
                        key = random.randint(1, 26)
                    else:
                        try:
                            int(inp)
                        except ValueError:
                            print("Please only enter a number or 'r'")
                        else:
                            key = int(inp)
                            mult = random.randint(0, 8)
                            key = key + (26*mult) - 1
                            check = True

    if __name__ == "__main__":
        choice = printOptions()
        if choice == 1:
            textChoice = textMenu()
            if choice == 1:
                show("text")
            elif choice == 2:
                modify("set", "text")
        elif choice == 2:
            cryptChoice = cryptMenu()
