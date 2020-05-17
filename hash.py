import math

class dex():
    def init(self):
        self.address = [none] * 200

    def show(self):
        for i in self.address:
            print(self.address[i])

    def dexadd(self, number, hash):
        self.address[hash] = number

    def getnum():
        check = False
        while check == False:
            print("OwO c-cans I haves a 5 dimgit numbwer pleams")
            number = input(">")
            try:
                int(number)
            except ValueError:
                print("nyeh~~ T-that's notsh a weal number -w-")
            else:
                if len(str(number)) != 5:
                    print("I-it's nwot the right legwth twt")
                else:
                    check = True

        number = int(number)
        hasho = hash(number)
        return hasho

    def getmnum():
        check = False
        while check == False:
            print("How many random numbers would you like to hash?")
            loops = input(">")
            try:
                int(loops)
            except ValueError:
                print("Are you aware of what is a number?")
            else:
                if int(loops) > 0:
                    check = True
        for i in loops:
            hash(i)

    def hash(number):
        hasho = 3 * (number/1600)
        hasho = math.ceil(hasho)
        return hasho
        dexadd(hasho, number)

if __name__ == "__main__":
    dex1 = dex()
    while True:
        print("What would you like to do?")
        print("1) Input new number")
        print("2) Input multiple random numbers")
        print("3) Print address")
        ch = input(">")
        if ch == "1":
            number = dex.getnum()
            print("Your key is: ", number)
        elif ch == "2":
            dex.getmnum()
        elif ch == "3":
            dex1.show()
