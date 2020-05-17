import os
import random
import time
from random import shuffle

menu = True

try:
    with open("deck.txt") as f:
        lines = f.readlines()
except OSError:
    print("Deck file missing")
    input("Press enter to close")
    sys.exit

with open("deck.txt") as f:
        cards = f.readlines()

random.shuffle(cards)

while menu == True:
    m = input("Would you like to play (p), Reshuffle (r), or Quit (q) ")

    if m == "q":
        print("Quitting in 2 seconds")
        time.sleep(2)
        quit()
    elif m == "r":
        random.shuffle(cards)
        print("Cards shuffled")
    elif m == "p":
        menu = False
    else:
        print("Please enter one of the specified letters to continue")


p1cards = 2
p2cards = 2
p3cards = 2
p4cards = 2

p1c1 = int(cards.pop(0))

p1c2 = int(cards.pop(0))

p2c1 = int(cards.pop(0))

p2c2 = int(cards.pop(0))

p3c1 = int(cards.pop(0))

p3c2 = int(cards.pop(0))

p4c1 = int(cards.pop(0))

p4c2 = int(cards.pop(0))


print("It is player 1's turn")

turn = True

while turn == True:
    ss = input("Would you like to stick (t) or spin (p)")
    if ss == "t":
        turn = False
        
        if p1cards == 2:
            p1score = p1c1 + p1c2
        elif p1cards == 3:
            p1score = p1c1 + p1c2 + p1c3
        elif p1cards == 4:
            p1score = p1c1 + p1c2 + p1c3 + p1c4
        elif p1cards == 5:
            p1score = p1c1 + p1c2 + p1c3 + p1c4 + p1c5
        
    elif ss == "p":
        if p1cards == 2:
            p1cards = 3
            p1c3 = int(cards.pop(0))
            cards.pop (0)
            
        elif p1cards == 3:
            p1cards = 4
            p1c4 = int(cards.pop(0))
            
            
        elif p1cards == 4:
            p1cards = 5
            p1c5 = int(cards.pop(0))
            

        elif p1cards == 5:
            print("You already have the maximum number of cards in your hand")
    else:
        print("Please enter one of the specified letters")


print("It is player 2's turn")

turn = True

while turn == True:
    ss = input("Would you like to stick (t) or spin (p)")
    if ss == "t":
        turn = False
        
        if p2cards == 2:
            p2score = p2c1 + p2c2
        elif p2cards == 3:
            p2score = p2c1 + p2c2 + p2c3
        elif p2cards == 4:
            p2score = p2c1 + p2c2 + p2c3 + p2c4
        elif p2cards == 5:
            p2score = p2c1 + p2c2 + p2c3 + p2c4 + p2c5
        
    elif ss == "p":
        if p2cards == 2:
            p2cards = 3
            p2c3 = int(cards.pop(0))
            cards.pop (0)
            
        elif p2cards == 3:
            p2cards = 4
            p2c4 = int(cards.pop(0))
            
            
        elif p2cards == 4:
            p2cards = 5
            p2c5 = int(cards.pop(0))
            

        elif p2cards == 5:
            print("You already have the maximum number of cards in your hand")
    else:
        print("Please enter one of the specified letters")

print("It is player 3's turn")

turn = True

while turn == True:
    ss = input("Would you like to stick (t) or spin (p)")
    if ss == "t":
        turn = False
        
        if p3cards == 2:
            p3score = p3c1 + p3c2
        elif p3cards == 3:
            p3score = p3c1 + p3c2 + p3c3
        elif p3cards == 4:
            p3score = p3c1 + p3c2 + p3c3 + p3c4
        elif p3cards == 5:
            p3score = p3c1 + p3c2 + p3c3 + p3c4 + p3c5
        
    elif ss == "p":
        if p3cards == 2:
            p3cards = 3
            p3c3 = int(cards.pop(0))
            cards.pop (0)
            
        elif p3cards == 3:
            p3cards = 4
            p3c4 = int(cards.pop(0))
            
            
        elif p3cards == 4:
            p3cards = 5
            p3c5 = int(cards.pop(0))
            

        elif p3cards == 5:
            print("You already have the maximum number of cards in your hand")
    else:
        print("Please enter one of the specified letters")

print("It is player 4's turn")

turn = True

while turn == True:
    ss = input("Would you like to stick (t) or spin (p)")
    if ss == "t":
        turn = False
        
        if p4cards == 2:
            p4score = p4c1 + p4c2
        elif p4cards == 3:
            p4score = p4c1 + p4c2 + p4c3
        elif p4cards == 4:
            p4score = p4c1 + p4c2 + p4c3 + p4c4
        elif p4cards == 5:
            p4score = p4c1 + p4c2 + p4c3 + p4c4 + p4c5
        
    elif ss == "p":
        if p4cards == 2:
            p4cards = 3
            p4c3 = int(cards.pop(0))
            cards.pop (0)
            
        elif p4cards == 3:
            p4cards = 4
            p4c4 = int(cards.pop(0))
            
            
        elif p4cards == 4:
            p4cards = 5
            p4c5 = int(cards.pop(0))
            

        elif p3cards == 5:
            print("You already have the maximum number of cards in your hand")
    else:
        print("Please enter one of the specified letters")

if p4score > 21:
    p4score = 0 - (p4score - 21)

print("Player four's score is ", p4score, "!")

better = False

input("Player 1, do you think you scored better than player four?, (y/n) ")
input("Player 2, do you think you scored better than player four?, (y/n) ")
input("Player 3, do you think you scored better than player four?, (y/n) ")
input("Player 4, do you think you scored better than player four?, (y/n) ")

if p1score > 21:
    p1score = 0 - (p1score - 21)

if p2score > 21:
    p2score = 0 - (p2score - 21)

if p3score > 21:
    p3score = 0 - (p3score - 21)



p1place = 4
p2place = 4
p3place = 4
p4place = 4

if p1score > p2score:
    p1place = p1place -1
elif p1score < p2score:
    p2place = p2place -1
elif p1score == p2score:
    p1place = p1place -1
    p2place = p2place -1

if p1score > p3score:
    p1place = p1place -1
elif p1score < p3score:
    p3place = p3place -1
elif p1score == p3score:
    p1place = p1place -1
    p3place = p3place -1

if p1score > p4score:
    p1place = p1place -1
elif p1score < p4score:
    p4place = p4place -1
elif p1score == p4score:
    p1place = p1place -1
    p4place = p4place -1

if p2score > p3score:
    p2place = p2place -1
elif p2score < p3score:
    p3place = p3place -1
elif p2score == p3score:
    p2place = p2place -1
    p3place = p3place -1

if p2score > p4score:
    p2place = p2place -1
elif p2score < p4score:
    p4place = p4place -1
elif p2score == p4score:
    p2place = p2place -1
    p4place = p4place -1

if p3score > p4score:
    p3place = p3place -1
elif p3score < p4score:
    p4place = p4place -1
elif p3score == p4score:
    p3place = p3place -1
    p4place = p4place -1

print("Player 1 came in place ", p1place," with ", p1score, " points ")
print("Player 2 came in place ", p2place," with ", p2score, " points ")
print("Player 3 came in place ", p3place," with ", p3score, " points ")
print("Player 4 came in place ", p4place," with ", p4score, " points ")








