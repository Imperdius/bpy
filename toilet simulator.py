import random
print("Hello! Welcome to my toilet simulator!")
print("Press enter to continue")
h = input(">").lower()
no = False
noob = False
yes = False
if h == ("no"):
    print("You bumbling bafoon, you are an absolute idiot and a stupid member of the land")
    no = True
if h == ("obama"):
    print("Do you think you're funny? Do that again and you will lose you nae nae privleges")
    noob = True
if h == ("yes"):
    print("no")
    yes = True
else:
    yes = True
toiletmenu = True
flushes = 0
hp = 10
paper = 0
hpaper = 0
cons = 0
houses = 1
toilets = 0
contoilets = 1
fgain = 0
while True:
    while toiletmenu == True:
        print("---------------------------------------------------------------------------------------------------------------------------")
        print("TOILET ONLINE")
        print("enter 'f' for flush, 't' for toilet paper, 'p' to view property, and 's' for shop!")
        tmenu = input("> ").lower()
        if tmenu == ("f"):
            if noob == False:
                print("Toilet flushed successfully, you earned 1 flushcoin plus 1 for each piece of paper you flushed, per connected toilet flushed!")
                fgain = (hpaper + 1) * contoilets
                flushes = flushes + fgain
                fgain = 0
                hpaper = 0
                print("You now have ", flushes, " flushcoins")
            else:
                print("In your attempt to flush the toilet you punch yourself in the face. -1 HP")
                hp = hp -1
                print ("you now have ", hp, " hp left")
                if hp < 1:
                    print ("You have died and become a ghost. On the plus side you learned to flush a toilet, practice makes perfect")
        if tmenu == ("t"):
            if yes == False:
                if paper < 1:
                    print("Your toilet paper holder is empty")
                    print("You are currently holding", hpaper, "pieces of toilet paper")
                else:
                    print("You took all of your toilet paper!")
                    hpaper = hpaper + paper
                    print("You are holding", hpaper, "pieces of toilet paper")
                    paper = 0
            else:
                print("You reach for the toilet paper, however, you have placed it on the holder the wrong way around. Society abandons you.")
                yes = False
                no = True
        if tmenu == ("s"):
            if no == True:
                print("On your way to the local shop you are spotted by police who arrest you and take you to a mental facility. The mental facility is titled toilet simulator. You walk to the shops")
                no = False
            print("Welcome to the shops, here you can buy stuff with flushcoins you have collected")
            print("Press 'x' to purchase and open a standard toilet box")
            print("Press 'y' to purchase and open a deluxe toilet box")
            print("More toilet boxes and toilet season pass coming soon")
            print("If you want to go back press enter.")
            smenu = input(">").lower()
            if smenu == ("x"):
                if flushes > 4:
                    lootrnd = (random.randint(60, 100) // 20) + (random.randint(20, 40) % random.randint(2, 10))
                    lootrnd = int(lootrnd)
                    lootrnd = lootrnd * 2
                    flushes = flushes - 5
                    if lootrnd == 55:
                        print("JACKPOT!!!!")
                        print("You have recived 5 houses, 5 toilets and 5 flush connectors")
                        toilets = toilets + 5
                        houses = houses + 5
                        cons = cons + 5
                    else:
                        paper = paper + lootrnd
                        print("You gained ", lootrnd, " pieces of toilet paper, you now have ", paper, " pieces of toilet paper")
                else:
                    print("You need", (5 - flushes), "more flush coins to purchase a standard lootbox")
            elif smenu == ("y"):
                if flushes > 19:
                    flushes = flushes - 20
                    lootrnd = random.randint(1, 10)
                    if lootrnd <= 4:
                        print("You gained", lootrnd, "toilets")
                        toilets = toilets + lootrnd
                    elif lootrnd == 5 or lootrnd == 6 or lootrnd == 7 or lootrnd == 8:
                        print("You gained 1 toilet connector")
                        cons = cons + 1
                    elif lootrnd == 9:
                        print("You gained 1 house")
                        houses = houses + 1
                    else:
                        print("Better luck next time!")
                else:
                    print("You need ", (20 - flushes), " more flushcoins to purchase a deluxe toilet box")
        if tmenu == ("p"):
            print("You currently have ", houses, " houses")
            print("You currently have ", toilets, " unconnected toilets")
            print("You currently have ", cons, " connectors")
            print("You currently have ", contoilets, " connected toilets")
            print("Press 'a' to connect a toilet, rember there a maximum of 5 toilets connected per house owned")
            print("Otherwise, press enter to cancel")
            a = input(">").lower()
            if a == "a":
                if toilets > 0:
                    if cons > 0:
                        if (contoilets // houses) < 5:
                            toilets = toilets - 1
                            cons = cons - 1
                            contoilets = contoilets + 1
                            print("Successfully connected toilet, you now have ", contoilets, " connected toilets")
                        else:
                            print("All of your houses are full")
                    else:
                        print("You don't have enough toilet connectors")
                else:
                    print("You don't have enough toilets")
