#  ____        _   _   _        ____  _     _
# | __ )  __ _| |_| |_| | ___  / ___|| |__ (_)_ __
# |  _ \ / _` | __| __| |/ _ \ \___ \| '_ \| | '_ \
# | |_) | (_| | |_| |_| |  __/  ___) | | | | | |_) |
# |____/ \__,_|\__|\__|_|\___| |____/|_| |_|_| .__/
#                                            |_|

import random

#todo
# 1. better ai fire
# 2. refactor


class Game():
    def __init__(self):
        self.boardSize = 10
        self.playerShipBoard     = [["*" for i in range(self.boardSize)] for j in range(self.boardSize)]
        self.playerTargetBoard   = [["*" for i in range(self.boardSize)] for j in range(self.boardSize)]
        self.aiShipBoard         = [["*" for i in range(self.boardSize)] for j in range(self.boardSize)]
        self.aiTargetBoard       = [["*" for i in range(self.boardSize)] for j in range(self.boardSize)]

        self.playerShipPlaced = 0
        self.aiShipPlaced = 0

        self.playerFireList = []
        self.aiFireList = []

        self.playerHitCount= 0
        self.aiHitCount      = 0
        self.playGame = True
        self.winner = ""

        self.directions=['n', 's', 'e', 'w']
        # Ships = [['c','c','c','c','c'],['b','b','b','b'],['r','r','r'],['s','s','s'],['d','d']] #note

        self.playerShipList=[0,0,0,0,0]
        self.aiShipList = [0,0,0,0,0]
        self.displayOnce = [False] * 10

        self.randomPlace = False




    def Intro(self):
        print("  ____        _   _   _        ____  _     _         ")
        print(" | __ )  __ _| |_| |_| | ___  / ___|| |__ (_)_ __    ")
        print(" |  _ \ / _` | __| __| |/ _ \ \___ \| '_ \| | '_ \   ")
        print(" | |_) | (_| | |_| |_| |  __/  ___) | | | | | |_) |  ")
        print(" |____/ \__,_|\__|\__|_|\___| |____/|_| |_|_| .__/   ")
        print("                                            |_|      ")
        print("         A Console Based Game of Death!              ")
        print("      By: Bradley Morton and George Meier            ")

    def validSpotPlayer(self, x, y): # checks if on board and water
        valid = False
        if x>=0 and x<self.boardSize and y>=0 and y<self.boardSize and self.playerShipBoard[x][y] not in ['c','b','r','s','d']:
            valid = True
        return valid

    def validSpotAi(self, x, y): # checks if on board and water
        valid = False
        if x>=0 and x<self.boardSize and y<self.boardSize and self.aiShipBoard[x][y] not in ['c','b','r','s','d']:
            valid = True
        return valid

    def validPlacementPlayer(self, x, y):
        if self.validSpotPlayer(x, y) == False:
            return False
        elif self.playerShipBoard[x][y] != "*":
            return False
        return True

    def validPlacementAi(self, x, y):
        if self.validSpotAi(x, y) == False:
            return False
        elif self.aiShipBoard[x][y] != "*":
            return False
        return True


    def place(self, team, x, y, direction, letter): #n, s flip
        if team == "player":
            if letter == 'c' :
                if direction == 's' and self.validPlacementPlayer(x, y) and self.validPlacementPlayer(x, y + 1)and self.validPlacementPlayer(x, y + 2) and self.validPlacementPlayer(x, y + 3) and self.validPlacementPlayer(x, y + 4):
                    for i in range(0,5):
                        self.playerShipBoard[x][y+i] = letter
                    return True
                elif direction == 'n' and self.validPlacementPlayer(x, y) and self.validPlacementPlayer(x, y - 1)and self.validPlacementPlayer(x, y - 2) and self.validPlacementPlayer(x, y - 3) and self.validPlacementPlayer(x, y - 4):
                    for i in range(0,5):
                        self.playerShipBoard[x][y-i] = letter
                    return True
                elif direction == 'e' and self.validPlacementPlayer(x, y) and self.validPlacementPlayer(x + 1, y)and self.validPlacementPlayer(x + 2, y) and self.validPlacementPlayer(x + 3, y) and self.validPlacementPlayer(x + 4, y):
                    for i in range(0,5):
                        self.playerShipBoard[x+i][y] = letter
                    return True
                elif direction == 'w' and self.validPlacementPlayer(x, y) and self.validPlacementPlayer(x - 1, y)and self.validPlacementPlayer(x - 2, y) and self.validPlacementPlayer(x - 3, y) and self.validPlacementPlayer(x - 4, y):
                    for i in range(0,5):
                        self.playerShipBoard[x-i][y] = letter
                    return True
            elif letter == 'b':
                if direction == 's' and self.validPlacementPlayer(x, y) and self.validPlacementPlayer(x, y + 1)and self.validPlacementPlayer(x, y + 2) and self.validPlacementPlayer(x, y + 3):
                    for i in range(0,4):
                        self.playerShipBoard[x][y+i] = letter
                    return True
                elif direction == 'n' and self.validPlacementPlayer(x, y) and self.validPlacementPlayer(x, y - 1)and self.validPlacementPlayer(x, y - 2) and self.validPlacementPlayer(x, y - 3):
                    for i in range(0,4):
                        self.playerShipBoard[x][y-i] = letter
                    return True
                elif direction == 'e' and self.validPlacementPlayer(x, y) and self.validPlacementPlayer(x + 1, y)and self.validPlacementPlayer(x + 2, y) and self.validPlacementPlayer(x + 3, y):
                    for i in range(0,4):
                        self.playerShipBoard[x+i][y] = letter
                    return True
                elif direction == 'w' and self.validPlacementPlayer(x, y) and self.validPlacementPlayer(x - 1, y)and self.validPlacementPlayer(x - 2, y) and self.validPlacementPlayer(x - 3, y):
                    for i in range(0,4):
                        self.playerShipBoard[x-i][y] = letter
                    return True
            elif letter == 'r':
                if direction == 's' and self.validPlacementPlayer(x, y) and self.validPlacementPlayer(x, y + 1)and self.validPlacementPlayer(x, y + 2):
                    for i in range(0,3):
                        self.playerShipBoard[x][y+i] = letter
                    return True
                elif direction == 'n' and self.validPlacementPlayer(x, y) and self.validPlacementPlayer(x, y - 1)and self.validPlacementPlayer(x, y - 2):
                    for i in range(0,3):
                        self.playerShipBoard[x][y-i] = letter
                    return True
                elif direction == 'e' and self.validPlacementPlayer(x, y) and self.validPlacementPlayer(x + 1, y)and self.validPlacementPlayer(x + 2, y):
                    for i in range(0,3):
                        self.playerShipBoard[x+i][y] = letter
                    return True
                elif direction == 'w' and self.validPlacementPlayer(x, y) and self.validPlacementPlayer(x - 1, y)and self.validPlacementPlayer(x - 2, y):
                    for i in range(0,3):
                        self.playerShipBoard[x-i][y] = letter
                    return True
            elif letter == 's':
                if direction == 's' and self.validPlacementPlayer(x, y) and self.validPlacementPlayer(x, y + 1)and self.validPlacementPlayer(x, y + 2):
                    for i in range(0,3):
                        self.playerShipBoard[x][y+i] = letter
                    return True
                elif direction == 'n' and self.validPlacementPlayer(x, y) and self.validPlacementPlayer(x, y - 1)and self.validPlacementPlayer(x, y - 2):
                    for i in range(0,3):
                        self.playerShipBoard[x][y-i] = letter
                    return True
                elif direction == 'e' and self.validPlacementPlayer(x, y) and self.validPlacementPlayer(x + 1, y)and self.validPlacementPlayer(x + 2, y):
                    for i in range(0,3):
                        self.playerShipBoard[x+i][y] = letter
                    return True
                elif direction == 'w' and self.validPlacementPlayer(x, y) and self.validPlacementPlayer(x - 1, y)and self.validPlacementPlayer(x - 2, y):
                    for i in range(0,3):
                        self.playerShipBoard[x-i][y] = letter
                    return True
            elif letter == 'd':
                if direction == 's' and self.validPlacementPlayer(x, y) and self.validPlacementPlayer(x, y + 1):
                    for i in range(0,2):
                        self.playerShipBoard[x][y+i] = letter
                    return True
                elif direction == 'n' and self.validPlacementPlayer(x, y) and self.validPlacementPlayer(x, y - 1):
                    for i in range(0,2):
                        self.playerShipBoard[x][y-i] = letter
                    return True
                elif direction == 'e' and self.validPlacementPlayer(x, y) and self.validPlacementPlayer(x + 1, y):
                    for i in range(0,2):
                        self.playerShipBoard[x+i][y] = letter
                    return True
                elif direction == 'w' and self.validPlacementPlayer(x, y) and self.validPlacementPlayer(x - 1, y):
                    for i in range(0,2):
                        self.playerShipBoard[x-i][y] = letter
                    return True
        elif team == "ai":
            if letter == 'c' :
                if direction == 's' and self.validPlacementAi(x, y) and self.validPlacementAi(x, y + 1)and self.validPlacementAi(x, y + 2) and self.validPlacementAi(x, y + 3) and self.validPlacementAi(x, y + 4):
                    for i in range(0,5):
                        self.aiShipBoard[x][y+i] = letter
                    return True
                elif direction == 'n' and self.validPlacementAi(x, y) and self.validPlacementAi(x, y - 1)and self.validPlacementAi(x, y - 2) and self.validPlacementAi(x, y - 3) and self.validPlacementAi(x, y - 4):
                    for i in range(0,5):
                        self.aiShipBoard[x][y-i] = letter
                    return True
                elif direction == 'e' and self.validPlacementAi(x, y) and self.validPlacementAi(x + 1, y)and self.validPlacementAi(x + 2, y) and self.validPlacementAi(x + 3, y) and self.validPlacementAi(x + 4, y):
                    for i in range(0,5):
                        self.aiShipBoard[x+i][y] = letter
                    return True
                elif direction == 'w' and self.validPlacementAi(x, y) and self.validPlacementAi(x - 1, y)and self.validPlacementAi(x - 2, y) and self.validPlacementAi(x - 3, y) and self.validPlacementAi(x - 4, y):
                    for i in range(0,5):
                        self.aiShipBoard[x-i][y] = letter
                    return True
            elif letter == 'b':
                if direction == 's' and self.validPlacementAi(x, y) and self.validPlacementAi(x, y + 1)and self.validPlacementAi(x, y + 2) and self.validPlacementAi(x, y + 3):
                    for i in range(0,4):
                        self.aiShipBoard[x][y+i] = letter
                    return True
                elif direction == 'n' and self.validPlacementAi(x, y) and self.validPlacementAi(x, y - 1)and self.validPlacementAi(x, y - 2) and self.validPlacementAi(x, y - 3):
                    for i in range(0,4):
                        self.aiShipBoard[x][y-i] = letter
                    return True
                elif direction == 'e' and self.validPlacementAi(x, y) and self.validPlacementAi(x + 1, y)and self.validPlacementAi(x + 2, y) and self.validPlacementAi(x + 3, y):
                    for i in range(0,4):
                        self.aiShipBoard[x+i][y] = letter
                    return True
                elif direction == 'w' and self.validPlacementAi(x, y) and self.validPlacementAi(x - 1, y)and self.validPlacementAi(x - 2, y) and self.validPlacementAi(x - 3, y):
                    for i in range(0,4):
                        self.aiShipBoard[x-i][y] = letter
                    return True
            elif letter == 'r':
                if direction == 's' and self.validPlacementAi(x, y) and self.validPlacementAi(x, y + 1)and self.validPlacementAi(x, y + 2):
                    for i in range(0,3):
                        self.aiShipBoard[x][y+i] = letter
                    return True
                elif direction == 'n' and self.validPlacementAi(x, y) and self.validPlacementAi(x, y - 1)and self.validPlacementAi(x, y - 2):
                    for i in range(0,3):
                        self.aiShipBoard[x][y-i] = letter
                    return True
                elif direction == 'e' and self.validPlacementAi(x, y) and self.validPlacementAi(x + 1, y)and self.validPlacementAi(x + 2, y):
                    for i in range(0,3):
                        self.aiShipBoard[x+i][y] = letter
                    return True
                elif direction == 'w' and self.validPlacementAi(x, y) and self.validPlacementAi(x - 1, y)and self.validPlacementAi(x - 2, y):
                    for i in range(0,3):
                        self.aiShipBoard[x-i][y] = letter
                    return True
            elif letter == 's':
                if direction == 's' and self.validPlacementAi(x, y) and self.validPlacementAi(x, y + 1)and self.validPlacementAi(x, y + 2):
                    for i in range(0,3):
                        self.aiShipBoard[x][y+i] = letter
                    return True
                elif direction == 'n' and self.validPlacementAi(x, y) and self.validPlacementAi(x, y - 1)and self.validPlacementAi(x, y - 2):
                    for i in range(0,3):
                        self.aiShipBoard[x][y-i] = letter
                    return True
                elif direction == 'e' and self.validPlacementAi(x, y) and self.validPlacementAi(x + 1, y)and self.validPlacementAi(x + 2, y):
                    for i in range(0,3):
                        self.aiShipBoard[x+i][y] = letter
                    return True
                elif direction == 'w' and self.validPlacementAi(x, y) and self.validPlacementAi(x - 1, y)and self.validPlacementAi(x - 2, y):
                    for i in range(0,3):
                        self.aiShipBoard[x-i][y] = letter
                    return True
            elif letter == 'd':
                if direction == 's' and self.validPlacementAi(x, y) and self.validPlacementAi(x, y + 1):
                    for i in range(0,2):
                        self.aiShipBoard[x][y+i] = letter
                    return True
                elif direction == 'n' and self.validPlacementAi(x, y) and self.validPlacementAi(x, y - 1):
                    for i in range(0,2):
                        self.aiShipBoard[x][y-i] = letter
                    return True
                elif direction == 'e' and self.validPlacementAi(x, y) and self.validPlacementAi(x + 1, y):
                    for i in range(0,2):
                        self.aiShipBoard[x+i][y] = letter
                    return True
                elif direction == 'w' and self.validPlacementAi(x, y) and self.validPlacementAi(x - 1, y):
                    for i in range(0,2):
                        self.aiShipBoard[x-i][y] = letter
                    return True
        return False

    def fire(self,team,x,y):
        if team == "player":
            if x>=0 and x<self.boardSize and y>=0 and y<self.boardSize and self.aiShipBoard[x][y] in ('c', 'b', 'r', 's', 'd') : # hit
                self.aiHitCount          += 1
                self.markShipList("player",self.aiShipBoard[x][y])
                self.playerTargetBoard[x][y] = 'X'
                self.aiShipBoard[x][y]       = 'X'
                self.playerFireList.append([x,y])
            elif self.validSpotAi(x, y):                                # miss
                self.playerTargetBoard[x][y] = '@'
                self.aiShipBoard[x][y]       = '@'
                self.playerFireList.append([x,y])
        elif team == "ai":
            if x>=0 and x<self.boardSize and y>=0 and y<self.boardSize and self.playerShipBoard[x][y] in ('c', 'b', 'r', 's', 'd') : # hit
                self.playerHitCount              += 1
                self.markShipList("ai", self.playerShipBoard[x][y])
                self.aiTargetBoard[x][y]     = 'X'
                self.playerShipBoard[x][y]   = 'X'
                self.aiFireList.append([x,y])
            elif self.validSpotPlayer(x, y):                                    # miss
                self.aiTargetBoard[x][y]   = '@'
                self.playerShipBoard[x][y] = '@'
                self.aiFireList.append([x, y])
        return

    def markShipList(self,team,char,):
        if team == "player":
            if char == 'c':
                self.aiShipList[0] += 1
            elif char == 'b':
                self.aiShipList[1] += 1
            elif char == 'r':
                self.aiShipList[2] += 1
            elif char == 's':
                self.aiShipList[3] += 1
            elif char == 'd':
                self.aiShipList[4] += 1
        elif team == "ai":
            if char == 'c':
                self.playerShipList[0] += 1
            elif char == 'b':
                self.playerShipList[1] += 1
            elif char == 'r':
                self.playerShipList[2] += 1
            elif char == 's':
                self.playerShipList[3] += 1
            elif char == 'd':
                self.playerShipList[4] += 1

    def checkSunkShip(self):
        if self.aiShipList[0] == 5 and self.displayOnce[0]==False:
            print("player sunk ai's carrier")
            self.displayOnce[0]=True
        elif self.aiShipList[1] == 4 and self.displayOnce[1]==False:
            print("player sunk ai's battleship")
            self.displayOnce[1] = True
        elif self.aiShipList[2] == 3 and self.displayOnce[2]==False:
            print("player sunk ai's cruiser")
            self.displayOnce[2] = True
        elif self.aiShipList[3] == 3 and self.displayOnce[3]==False:
            print("player sunk ai's sub")
            self.displayOnce[3] = True
        elif self.aiShipList[4] == 2 and self.displayOnce[4]==False:
            print("player sunk ai's destroyer")
            self.displayOnce[4] = True

        elif self.playerShipList[0] == 5 and self.displayOnce[5]==False:
            print("ai sunk player's carrier")
            self.displayOnce[5] = True
        elif self.playerShipList[1] == 4 and self.displayOnce[6]==False:
            print("ai sunk player's battleship")
            self.displayOnce[6] = True
        elif self.playerShipList[2] == 3 and self.displayOnce[7]==False:
            print("ai sunk player's cruiser")
            self.displayOnce[7] = True
        elif self.playerShipList[3] == 3 and self.displayOnce[8]==False:
            print("ai sunk player's sub")
            self.displayOnce[8] = True
        elif self.playerShipList[4] == 2 and self.displayOnce[9]==False:
            print("ai sunk player's destroyer")
            self.displayOnce[9] = True

    def checkWin(self):
        if self.playerHitCount == 17:
            self.playGame = False
            self.winner = "AI WINS!"
        elif self.aiHitCount == 17:
            self.playGame = False
            self.winner = "PLAYER WINS!"
        return


    def draw(self, team):
        if team == "player":
            print("This is the player target board")
            for y in range(self.boardSize):
                for x in range(self.boardSize):
                    print(self.playerTargetBoard[x][y], end = '')
                print("")
            print("This is the player board")
            for y in range(self.boardSize):
                for x in range(self.boardSize):
                    print(self.playerShipBoard[x][y], end = '')
                print("")
        elif team == "ai":
            print("This is the ai target board")
            for y in range(self.boardSize):
                for x in range(self.boardSize):
                    print(self.aiTargetBoard[x][y], end = '')
                print("")
            print("This is the ai board")
            for y in range(self.boardSize):
                for x in range(self.boardSize):
                    print(self.aiShipBoard[x][y], end = '')
                print("")
        return


#  _____ _____ ____ _____ ____
# |_   _| ____/ ___|_   _/ ___|
#   | | |  _| \___ \ | | \___ \
#   | | | |___ ___) || |  ___) |
#   |_| |_____|____/ |_| |____/


game = Game()

#test place piece in invalid spot
print("TEST: player place ship in invaid spot")
if game.place("player", 0, 0, 'e', 'r')==game.place("player", 0, 0, 'e', 'c'):
    print("Fail")
else:
    print("Pass")

print("TEST: ai place ship in invaid spot")
if game.place("ai", 0, 0, 'e', 'c')==game.place("ai", 0, 0, 'e', 'd'):
    print("Fail")
else:
    print("Pass")

#test firing works
print("TEST: player fire")
game.fire("player",0,0)
if game.aiShipBoard[0][0]=='X' and game.playerTargetBoard[0][0]=='X':
    print("Pass")
else:
    print("Fail")

print("TEST: ai fire")
game.fire("ai",0,0)
if game.playerShipBoard[0][0]=='X' and game.aiTargetBoard[0][0]=='X':
    print("Pass")
else:
    print("Fail")

# #test sink ballteship
game.place("ai", 0, 9, 'e', 'd')
game.fire("player", 1,9)
game.fire("player",0,9)
print("TEST: player sink ai destroyer")
if game.aiShipList[4]==2 :
    print("Pass")
else:
    print("Fail")

game.place("player", 0, 9, 'e', 'd')
game.fire("ai", 1,9)
game.fire("ai",0,9)
print("TEST: ai sink player destroyer")
if game.playerShipList[4]==2 :
    print("Pass")
else:
    print("Fail")


# #test win game
game.place("ai", 0, 4, 'e', 'c')
game.place("ai", 0, 2, 'e', 'b')
game.place("ai", 0, 3, 'e', 's')
game.fire("player",1,0)
game.fire("player",2,0)
game.fire("player",3,0)
game.fire("player",4,0)


game.fire("player",0,2)
game.fire("player",1,2)
game.fire("player",2,2)
game.fire("player",3,2)

game.fire("player",0,3)
game.fire("player",1,3)
game.fire("player",2,3)

game.fire("player",0,4)
game.fire("player",1,4)
game.fire("player",2,4)
game.fire("player",3,4)
game.fire("player",4,4)

print("TEST: player wins")
if game.winner=="player":
    print("Fail")
else:
    print("Pass")



























