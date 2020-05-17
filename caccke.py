import math
global orders
orders = []

class cakes:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def getarea(self):
        area = (math.pi * (self.radius ** 2)) + (math.pi * self.height * (2 * self.radius))
        return area

    def getcustomarea(self, cradius, cheight):
        area = (math.pi * (cradius ** 2)) + (math.pi * cheight * (2 * cradius))
        return area

class order:
    def __init__(self):
        self.small = 0
        self.medium = 0
        self.large = 0
        self.custom = 0
        self.totalcakes = 0
        self.totalarea = 0

    def addcake(self, type):
        self.totalcakes = self.totalcakes + 1
        if type == "s":
            self.small = self.small + 1
            self.totalarea = self.totalarea + small.getarea()
        elif type == "m":
            self.medium = self.medium + 1
            self.totalarea = self.totalarea + medium.getarea()
        elif type == "l":
            self.large = self.large + 1
            self.totalarea = self.totalarea + big.getarea()
        else:
            self.custom = self.custom + 1

    def addcustom(self, type, cradius, cheight):
        self.custom = self.custom + 1
        self.totalarea = self.totalarea + large.getcustomarea(cradius, cheight)

    def printorder(self, i):
        print("---------------------------------------------------")
        print("For order", (orders.index(i)) + 1)
        print("Small cakes: ", self.small)
        print("Medium cakes: ", self.medium)
        print("Large cakes: ", self.large)
        print("Other cakes: ", self.custom)
        print("Total cakes: ", self.totalcakes)
        print("Total area: ", self.totalarea)
        butter = self.ingredients("b")
        sugar = self.ingredients("s")
        milk = self.ingredients("m")
        print("Butter needed: ", butter, "g")
        print("Sugar needed: ", sugar, "g")
        print("milk needed: ", milk, "table spoons")
        print("---------------------------------------------------")

    def ingredients(self, ingredient):
        if ingredient == "b":
            return math.ceil((self.totalarea / 180) * 140)
        if ingredient == "s":
            return math.ceil((self.totalarea / 180) * 280)
        if ingredient == "m":
            return math.ceil((self.totalarea / 180) * 2)

def createneworder():
    oname = order()
    orders.extend([oname])
    total = 0
    quantity = quantitymenu()
    sizemenu(quantity, oname)

def quantitymenu():
    qmenu = False
    while qmenu == False:
        print("Please enter the quantity of cakes")
        q = input(">")
        try:
            int(q)
        except ValueError:
            print("Please enter a number")
        else:
            q = int(q)
            if q <= 0:
                print("Please enter a value greater than 0")
            else:
                print("You have chosen ", q, " cakes, enter 'y' to confirm")
                conf = input(">")
                if conf.lower() == "y":
                    return q

def sizemenu(quantity, oname):
    for i in range (1, quantity + 1):
        smenu = False
        while smenu == False:
            print("Please enter a cake size for cake", i, " (s)mall, (m)edium, (l)arge, or (c)ustom")
            ctype = input(">")
            if isinstance(ctype, str):
                smenu = True
                if ctype.lower() == "s":
                    oname.addcake("s")
                elif ctype.lower() == "m":
                    oname.addcake("m")
                elif ctype.lower() == "l":
                    oname.addcake("l")
                elif ctype.lower() == "c":
                    rhmenu = False
                    while rhmenu == False:
                        print("Please enter the cake radius")
                        cradius = input(">")
                        try:
                            cradius = int(cradius)
                        except ValueError:
                            print("Please enter a number")
                        else:
                            int(cradius)
                            if cradius > 0:
                                print("Please enter the cake height")
                                cheight = input(">")
                                try:
                                    int(cheight)
                                except ValueError:
                                    print("Please enter a number")
                                else:
                                    cheight = int(cheight)
                                    if cheight > 0:
                                        rhmenu = True
                                        oname.addcake("c")
                                    else:
                                        print("Please enter a value greater then 0")
                            else:
                                print("Please enter a value greater then 0")
                else:
                    smenu = False
                    print("Please enter either 's', 'm', 'l' or 'c'")
            else:
                print("Please enter a letter")

if __name__ == '__main__':
    small = cakes(4, 2)
    medium = cakes(7.5, 4)
    big = cakes(10, 7)
    while True:
        mmenu = False
        while mmenu == False:
            print("Would you like to (v)iew orders or (c)reate a new order?")
            choice = input(">")
            if isinstance(choice, str):
                if choice.lower() == "v":
                    for i in orders:
                        i.printorder(i)
                elif choice.lower() == "c":
                    createneworder()
                else:
                    print("Please enter either 'c' or 'v'")
            else:
                print("Please only enter either 'c' or 'v'")
