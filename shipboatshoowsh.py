import os
import random
def displaymenu():
    print("What would you like to do?")
    print("1) Play")
    print("9) Quit")
    choice = input(">")
    return choice

def playgame():
    rows = 8
    columns = 8
    botBoard = [[0 for i in range(columns)] for j in range(rows)]
    mannBoard = [[0 for i in range(columns)] for j in range(rows)]

    boatShortAnchorX = random.randint(0, 7)
    boatShortAnchorY = random.randint(0, 7)
    boatShortDir = random.randint(1, 4)

    boatMediumAnchorX = random.randint(0, 7)
    boatMediumAnchorY = random.randint(0, 7)
    boatMediumDir = random.randint(1, 4)

    if boatMediumAnchorX > 5 and boatMediumDir == 1:
        boatShortDir = 3
    elif boatMediumAnchorX < 2 and boatMediumDir == 3:
        boatShortDir = 1

    if boatMediumAnchorY > 5 and boatMediumDir == 4:
        boatShortDir = 2
    elif boatMediumAnchorY < 2 and boatMediumDir == 2:
        boatShortDir = 4

    if boatMediumAnchorX > 4 and boatMediumDir == 1:
        boatShortDir = 3
    elif boatMediumAnchorX < 3 and boatMediumDir == 3:
        boatShortDir = 1

    if boatMediumAnchorY > 4 and boatMediumDir == 4:
        boatShortDir = 2
    elif boatMediumAnchorY < 3 and boatMediumDir == 2:
        boatShortDir = 4


    botBoard[boatShortAnchorX][boatShortAnchorY] = 1
    if boatShortDir == 1:
        boatShortAnchorX = boatShortAnchorX + 1
        botBoard[boatShortAnchorX][boatShortAnchorY] = 1
        boatShortAnchorX = boatShortAnchorX + 1
        botBoard[boatShortAnchorX][boatShortAnchorY] = 1
    elif boatShortDir == 2:
        boatShortAnchorY = boatShortAnchorY + 1
        botBoard[boatShortAnchorX][boatShortAnchorY] = 1
        boatShortAnchorY = boatShortAnchorY + 1
        botBoard[boatShortAnchorX][boatShortAnchorY] = 1
    elif boatShortDir == 3:
        boatShortAnchorX = boatShortAnchorX - 1
        botBoard[boatShortAnchorX][boatShortAnchorY] = 1
        boatShortAnchorX = boatShortAnchorX - 1
        botBoard[boatShortAnchorX][boatShortAnchorY] = 1
    elif boatShortDir == 4:
        boatShortAnchorY = boatShortAnchorY - 1
        botBoard[boatShortAnchorX][boatShortAnchorY] = 1
        boatShortAnchorY = boatShortAnchorY - 1
        botBoard[boatShortAnchorX][boatShortAnchorY] = 1

    botBoard[boatMediumAnchorX][boatMediumAnchorY] = 1
    if boatMediumDir == 1:
        boatMediumAnchorX = boatMediumAnchorX + 1
        botBoard[boatMediumAnchorX][boatMediumAnchorY] = 1
        boatMediumAnchorX = boatMediumAnchorX + 1
        botBoard[boatMediumAnchorX][boatMediumAnchorY] = 1
        boatMediumAnchorX = boatMediumAnchorX + 1
        botBoard[boatMediumAnchorX][boatMediumAnchorY] = 1
    elif boatMediumDir == 2:
        boatMediumAnchorY = boatMediumAnchorY + 1
        botBoard[boatMediumAnchorX][boatMediumAnchorY] = 1
        boatMediumAnchorY = boatMediumAnchorY + 1
        botBoard[boatMediumAnchorX][boatMediumAnchorY] = 1
        boatMediumAnchorY = boatMediumAnchorY + 1
        botBoard[boatMediumAnchorX][boatMediumAnchorY] = 1
    elif boatMediumDir == 3:
        boatMediumAnchorX = boatMediumAnchorX - 1
        botBoard[boatMediumAnchorX][boatMediumAnchorY] = 1
        boatMediumAnchorX = boatMediumAnchorX - 1
        botBoard[boatMediumAnchorX][boatMediumAnchorY] = 1
        boatMediumAnchorX = boatMediumAnchorX - 1
        botBoard[boatMediumAnchorX][boatMediumAnchorY] = 1
    elif boatMediumDir == 4:
        boatMediumAnchorY = boatMediumAnchorY - 1
        botBoard[boatMediumAnchorX][boatMediumAnchorY] = 1
        boatMediumAnchorY = boatMediumAnchorY - 1
        botBoard[boatMediumAnchorX][boatMediumAnchorY] = 1
        boatMediumAnchorY = boatMediumAnchorY - 1
        botBoard[boatMediumAnchorX][boatMediumAnchorY] = 1

    print(botBoard[0])
    print(botBoard[1])
    print(botBoard[2])
    print(botBoard[3])
    print(botBoard[4])
    print(botBoard[5])
    print(botBoard[6])
    print(botBoard[7])



if __name__ == "__main__":
    print("Welcome to battleships, the game where you battle ships!")
    print(r"""
                                     |__
                                     |\/
                                     ---
                                     / | [
                              !      | |||
                            _/|     _/|-++'
                        +  +--|    |--|--|_ |-
                     { /|__|  |/\__|  |--- |||__/
                    +---------------___[}-_===_.'____                 /\
                ____`-' ||___-{]_| _[}-  |     |_[___\==--            \/   _
 __..._____--==/___]_|__|_____________________________[___\==--____,------' .7
|                                                                           /
 \_________________________________________________________________________|
    """)
    mainMenu = False
    while mainMenu == False:
        choice = displaymenu()
        try:
            int(choice)
        except ValueError:
            print("Please enter a number")
        else:
            choice = int(choice)
            if choice > 0 and choice < 10:
                mainMenu == True
                if choice is not 9:
                    playgame()
                else:
                    sys.exit()
            else:
                print("Please enter a value between 1 and 9")
