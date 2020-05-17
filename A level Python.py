import random

class Card:
    def __init__(self,n=0):
        self._number = n
    def setNumber(self,n):
        self._number = n
    def getValue(self):
        value = 1 + self._number % 13
        return value
    def getSuit(self):
        suit = int(self._number / 13)
        return suit
    def getCardString(self):
        value = self.getValue()
        if value == 11:
            value = 'Jack'
        elif value == 12:
            value = 'Queen'
        elif value == 13:
            value = 'King'
        elif value == 1:
            value = 'Ace'
        else:
            value = str(value)

        suit = self.getSuit()
        if suit == 0:
            suit = 'Hearts'
        elif suit == 1:
            suit = 'Diamonds'
        elif suit == 2:
            suit = 'Clubs'
        elif suit == 3:
            suit = 'Spades'

        return 'Your card is the ' + value + ' of ' + suit

class Player:
    def __init__ (self, n=21):
        self._stickOnValue = n
        self._numberOfWins = 0
    def resetScore(self):
        self._numberOfWins = 0
    def newStickOnValue(self,n):
        self._stickOnValue = n
    def getStickOnValue(self):
        return(self._stickOnValue)
    def updateStickOnValue(self):
        print('Enter your sticking value, between 12 and 21: ')
        stickOn = int(input())
        while stickOn < 12 or stickOn > 21:
            print('Invalid, must be between 12 and 21. Try again: ')
            stickOn = int(input())
        self._stickOnValue = stickOn
    def updateNumberOfWins(self):
        self._numberOfWins = self._numberOfWins + 1
    def getNumberOfWins(self):
        return(self._numberOfWins)

class CardPile:
    def __init__(self):
        self._pile = []
    def printPile(self):
        for i in range(len(self._pile)):
            print(self._pile[i].getCardString())
        print()
    def clearPile(self):
        self._pile = []

class CardDeck(CardPile):
    def __init__(self):
        CardPile.__init__(self)
        self._dealt = 0
    def shuffle(self):
        random.seed()
        self.clearPile()
        chosen = [False]*52
        for i in range(52):
            choice = random.randint(0,51)
            while chosen[choice] == True:
                choice = random.randint(0,51)
            self._pile.append(Card(choice))
            chosen[choice] = True
        self._dealt = 0
        print('shuffled')
    def deal(self):
        if self._dealt == 52:
            print('Error, out of cards')
        else:
            card = self._pile[self._dealt]
            self._dealt = self._dealt + 1
            return(card)

class Hand(CardPile):
    def __init__(self):
        CardPile.__init__(self)
        self._score = 0
    def getValue(self,pictureTen):
        runningTotal = 0
        for i in range(len(self._pile)):
            temp = self._pile[i].getValue()
            if pictureTen and temp >= 10:
                temp = 10
            runningTotal = runningTotal + temp
        return runningTotal
    def addToPile(self,card):
        self._pile.append(card)
    def getScore(self):
        self._score = self.getValue(True)
        return(self._score)
    def clearHand(self):
        self.clearPile()
        self._score = 0



class Game():
    def __init__(self):
        self._deck = CardDeck()
        self._playerHand = Hand()
        self._dealerHand = Hand()
    def play(self,player,dealer):
        self._playerHand.clearHand()
        self._dealerHand.clearHand()
        self._deck.shuffle()
        for i in range(2):

            self._playerHand.addToPile(self._deck.deal())
            self._dealerHand.addToPile(self._deck.deal())
        while self._playerHand.getScore() < player.getStickOnValue():
            self._playerHand.addToPile(self._deck.deal())
        while self._dealerHand.getScore() < dealer.getStickOnValue():
            self._dealerHand.addToPile(self._deck.deal())

        print()
        print('Player Hand:')
        self._playerHand.printPile()
        print('Dealer Hand:')
        self._dealerHand.printPile()

        playerScore = self._playerHand.getScore()
        dealerScore = self._dealerHand.getScore()

        print('Player score = ', playerScore)
        print('Dealer score = ', dealerScore)

        if playerScore > 21: playerScore = 0
        if dealerScore > 21: dealerScore = 0

        if playerScore > dealerScore:
            print('Player wins!')
            player.updateNumberOfWins()
        else:
            print('Player loses')
            dealer.updateNumberOfWins()
    def getMenuChoice(self):
        print('')
        print('')
        print('####################');
        print('Welcome to Pontoon');
        print('')
        print('Choose from the following options:');
        print('1. Set your strategy');
        print('2. Test your strategy');
        print('3. Show stratergy')
        print('0. Quit');
        print('')
        print('Make your choice: ');
        choice = input()
        while choice not in ['0','1','2','3']:
            print('Invalid choice, please enter 1, 2, 3 or 0: ');
            choice = input()
        return(choice)



class Main():
    def __init__ (self):
        thisPlayer = Player()
        thisDealer = Player(16)
        thisGame = Game()
        choice = None
        while choice != '0':
            choice = thisGame.getMenuChoice()
            if choice == '1':
                print('Enter your sticking value, between 12 and 21: ');
                playerSticksOn = int(input())
                while (playerSticksOn < 12) or (playerSticksOn > 21):
                    print('Invalid, must be between 12 and 21. Try again: ')
                    playerSticksOn = int(input())
                thisPlayer.newStickOnValue(playerSticksOn)
            elif choice == '2':
                print('How many times do you want to run the game? (Max 30): ')
                loopSize = int(input())
                while (loopSize < 1) or (loopSize > 30):
                    print('Invalid, must be no more than 30. Try again: ')
                    loopSize = int(input())

                print('Automatic run through or step-by-step? (Enter ''a'' or ''s''): ')
                auto = input()
                while (auto != 'a') and (auto != 's'):
                    print('Invalid, enter either ''a'' or ''s'' (no speech marks): ');
                    auto = input()

                thisPlayer.resetScore()
                thisDealer.resetScore()
                for i in range(loopSize):
                    thisGame.play(thisPlayer,thisDealer)
                    print('Player ', thisPlayer.getNumberOfWins(), ' : ', thisDealer.getNumberOfWins(), ' Dealer')

                    if auto == 's':
                        print('Press return to continue')
                        input()

            elif choice == '3':
                print("Displaying stratergy:")
                print(thisPlayer.getStickOnValue())
        print()
        print('Thank you for playing the Pontoon Simulator');
        print('Press any key to close the program');
        print('####################');
        input()

thisMain = Main()
