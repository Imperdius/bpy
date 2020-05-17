#Skeleton Program for the AQA AS1 Summer 2016 examination
#this code should be used in conjunction with the Preliminary Material
#written by the AQA AS1 Programmer Team
#developed in a Python 3 programming environment

#Version Number 1.0

import random
global GameLost
global moves
moves = 1

def GetRowColumn():
  print()
  Columncheck = False
  while Columncheck == False:
    Column = input("Please enter column: ")
    try:
      int(Column)
    except ValueError:
      print("Please enter a number for column")
    else:
      Column = int(Column)
      if Column < 1 or Column > 10:
        print("Please enter a number between 1 and 10 for column")
      else:
        Columncheck = True
  Rowcheck = False
  while Rowcheck == False:
    Row = input("Please enter row: ")
    try:
      int(Row)
    except ValueError:
      print("Please enter a number for row")
    else:
      Row = int(Row)
      if Row < 1 or Row > 10:
        print("Please enter a number between 1 and 10 for row")
      else:
        Rowcheck = True
  Column = Column - 1
  Row = Row - 1
  print()
  return Row, Column

def MakePlayerMove(Board, Ships):
  global moves
  global GameLost
  Row, Column = GetRowColumn()
  if Board[Row][Column] == "m" or Board[Row][Column] == "h":
    print("Sorry, you have already shot at the square (" + str(Column + 1) + "," + str(Row + 1) + "). Please try again.")
  elif Board[Row][Column] == "-":
    moves = moves + 1
    print("Sorry, (" + str(Column + 1) + "," + str(Row + 1) + ") is a miss.")
    Board[Row][Column] = "m"
    if hard == True:
      if moves >= (maxmoves + 1):
        print("You missed while out of moves, you loose!")
        GameLost = True
  else:
    moves = moves + 1
    print("Hit at (" + str(Column + 1) + "," + str(Row + 1) + ").")
    Board[Row][Column] = "h"
  if hard == True:
    if moves == maxmoves:
      print("Out of moves! Miss now and you will loose!")
    elif moves == (maxmoves - 1):
      print("Last move")


def SetUpBoard():
  Board = []
  for Row in range(10):
    BoardRow = []
    for Column in range(10):
      BoardRow.append("-")
    Board.append(BoardRow)
  return Board

def LoadGame(Filename, Board):
  BoardFile = open(Filename, "r")
  for Row in range(10):
    Line = BoardFile.readline()
    for Column in range(10):
      Board[Row][Column] = Line[Column]
  BoardFile.close()

def PlaceRandomShips(Board, Ships):
  for Ship in Ships:
    Valid = False
    while not Valid:
      Row = random.randint(0, 9)
      Column = random.randint(0, 9)
      HorV = random.randint(0, 1)
      if HorV == 0:
        Orientation = "v"
      else:
        Orientation = "h"
      Valid = ValidateBoatPosition(Board, Ship, Row, Column, Orientation)
    print("Computer placing the " + Ship[0])
    PlaceShip(Board, Ship, Row, Column, Orientation)

def PlaceShip(Board, Ship, Row, Column, Orientation):
  if Orientation == "v":
    for Scan in range(Ship[1]):
      Board[Row + Scan][Column] = Ship[0][0]
  elif Orientation == "h":
    for Scan in range(Ship[1]):
      Board[Row][Column + Scan] = Ship[0][0]

def ValidateBoatPosition(Board, Ship, Row, Column, Orientation):
  if Orientation == "v" and Row + Ship[1] > 10:
    return False
  elif Orientation == "h" and Column + Ship[1] > 10:
    return False
  else:
    if Orientation == "v":
      for Scan in range(Ship[1]):
        if Board[Row + Scan][Column] != "-":
          return False
    elif Orientation == "h":
      for Scan in range(Ship[1]):
        if Board[Row][Column + Scan] != "-":
          return False
  return True

def CheckWin(Board):
  for Row in range(10):
    for Column in range(10):
      if Board[Row][Column] in ["A","B","S","D","P"]:
        return False
  return True

def PrintBoard(Board):
  print()
  global moves
  print("------------------------------------------------------------------------")
  print()
  print("Move number ", moves)
  print("The board looks like this: ")
  print()
  print ("   ", end="")
  for Column in range(10):
    print(" " + str(Column + 1) + "  ", end="")
  print()
  for Row in range(10):
    if Row < 9:
        print (str(Row + 1) + "   ", end="")
    else:
        print (str(Row + 1) + "  ", end="")
    for Column in range(10):
      if Board[Row][Column] == "-":
        print("x", end="")
      elif Board[Row][Column] in ["A","B","S","D","P"]:
        print("x", end="")
      else:
        print(Board[Row][Column], end="")
      if Column != 9:
        print(" | ", end="")
    print()

def DisplayMenu():
  print("MAIN MENU")
  print()
  print("1. Start new game")
  print("2. Load training game")
  print("3. Hard mode")
  print("9. Quit")
  print()

def GetMainMenuChoice():
  print("Please enter your choice: ", end="")
  Choice = input()
  try:
    int(Choice)
  except ValueError:
    print()
    print("Please enter a number")
  else:
    Choice = int(Choice)
  print()
  return Choice

def PlayGame(Board, Ships):
  global GameLost
  GameWon = False
  GameLost = False
  while not GameWon and not GameLost:
    PrintBoard(Board)
    MakePlayerMove(Board, Ships)
    GameWon = CheckWin(Board)
    if GameLost == True:
      print("You Lost by running out of moves")
    if GameWon:
      print("All ships sunk in ", moves, " moves!")
      print()

if __name__ == "__main__":
  TRAININGGAME = "Training.txt"
  MenuOption = 0
  while not MenuOption == 9:
    Board = SetUpBoard()
    Ships = [["Aircraft Carrier", 5], ["Battleship", 4], ["Submarine", 3], ["Destroyer", 3], ["Patrol Boat", 2], ["Battlebus", 4]]
    DisplayMenu()
    MenuOption = GetMainMenuChoice()
    if MenuOption == 1:
      hard = False
      PlaceRandomShips(Board, Ships)
      PlayGame(Board,Ships)
    if MenuOption == 2:
      LoadGame(TRAININGGAME, Board)
      PlayGame(Board, Ships)
    if MenuOption == 3:
      hard = True
      print("Enter hard mode difficulty (1-5)")
      diffcheck = False
      while diffcheck == False:
        difficulty = input("Please enter a difficulty: ")
        try:
          int(difficulty)
        except ValueError:
          print("Please enter a number")
        else:
          difficulty = int(difficulty)
          if difficulty < 1 or difficulty > 5:
            print("Please enter one of the options")
          else:
            diffcheck = True
      maxmoves = (6 - difficulty) * 15
      print("Maximum moves : ", maxmoves)
      PlaceRandomShips(Board, Ships)
      PlayGame(Board,Ships)
    else:
      print("Please enter one of the options")
