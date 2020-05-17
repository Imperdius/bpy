global momentpoints
global collection
collection = []
momentpoints = 0
class moment:
    def __init__(self, owned, cringe, haha, relatable, selfaware, edgy):
        self.owned = owned
        self.cringe = cringe
        self.haha = haha
        self.relatable = relatable
        self.selfaware = selfaware
        self.edgy = edgy

    def search(self):
        print("Welcome to China's inetrnets servers, where would you like to search?")
        platform = input(">")
        if platform.lower() == "youtube":
            self.youtube()
        else:
            print("Sorry, this has been removed from China's internet server for saying that our leader looks like whinnie to pooh which he definatly does not")

    def youtube(self):
        global momentpoints
        print("You search on youtube for", self, "moments, an ad for borderlands 3 comes up")
        print("Buy borderlands 3 for 20 momentpoints? (y/n)")
        buy = imput(">")
        if buy.lower() == y:
            if borderlands3.searchcollection() == True:
                print("You already own borderlands 3")
            else:
                if momentpoints > 20:
                    momentpoints = momentpoints - 20
                    borderlands3.additem()
                    print("Bought successfully, you now have ", momentpoints, " momentpoints")
                else:
                    print("Not enough momentpoints")

        if self.relatable == True:
            print("Many cases of ", self, " moments were found on youtube, +25 momentpoints")
            momentpoints = momentpoints + 25
            print("you now have ", momentpoints, " momentpoints")
        elif slef.haha == True or self.edgy == True:
            print("Few cases of ", self, " were found on youtube, +15 momentpoints")
            momentpoints = momentpoints + 15
            print("you now have ", momentpoints, " momentpoints")
        else:
            print("No cases of ", self, " moments were found on youtube")

class collection:
    def __init__(self):
        self.__owned = False

    def additem(self):
        if self.__owned == False:
            self.__owned = True
            collection.extend([self])

    def searchcollection(self):
        if self.__owned == True:
            return True
        else:
            return False

def mainmenu():
    menu = False
    while menu == False:
        print("What would you like to do?")
        print("1) Search the internet")
        print("2) Open collection")
        print("3) Banking")
        choice = input(">")
        try:
            int(choice)
        except ValueError:
            print("Please enter a number")
        else:
            choice = int(choice)
            if choice == 1:
                print("What kinda of moment would you like to search for?")
                moment = input(">")
                moment.Search()
            elif choice == 2:
                print("")

if __name__ == "__main__":
    borderlands3 = collection()
    bruh = moment(True, False, True, True, True, False)
    while True:
        mainmenu()
