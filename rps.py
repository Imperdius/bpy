import random
pScore = 0
cScore = 0
while True:
    check = False
    while check == False:
        print ("Choose (R)ock, (P)aper or (S)cissors")
        pChoice = input(">").lower()

        if len(pChoice) != 1:
            print("Please only enter one character")
        elif pChoice != ("r") and pChoice != ("p") and pChoice != ("s"):
            print("Please only enter either R, P or S")
        else:
            check = True
    cChoice = random.randint(1,3)
    if cChoice == 1:
        print("The computer chose rock")
        if pChoice == ("r"):
            print("You chose rock")
            print("You drew with the computer")
        elif pChoice == ("p"):
            print("You chose paper")
            print("You beat the computer")
            pScore = pScore + 1
        elif pChoice == ("s"):
            print("You chose scissors")
            print("The compter beat you")
            cScore = cScore + 1
    elif cChoice == 2:
        print("The compter chose paper")
        if pChoice == ("r"):
            print("You chose rock")
            print("The compter beat you")
            cScore = cScore + 1
        elif pChoice == ("p"):
            print("You chose paper")
            print("You drew with the computer")
        elif pChoice == ("s"):
            print("You chose scissors")
            print("You beat the computer")
            pScore = pScore + 1
    elif cChoice == 3:
        print("The computer chose scissors")
        if pChoice == ("r"):
            print("You chose rock")
            print("You beat the computer")
            pScore = pScore + 1
        elif pChoice == ("p"):
            print("You chose paper")
            print("The compter beat you")
            cScore = cScore + 1
        elif pChoice == ("s"):
           print("You chose scissors")
           print("You drew with the computer")
    print("Player score is:", pScore, "!")
    print("Computer score is:", cScore, "!")
    print("--------------------------------------------------------------")
            
            
