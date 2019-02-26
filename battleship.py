#  ____        _   _   _        ____  _     _
# | __ )  __ _| |_| |_| | ___  / ___|| |__ (_)_ __
# |  _ \ / _` | __| __| |/ _ \ \___ \| '_ \| | '_ \
# | |_) | (_| | |_| |_| |  __/  ___) | | | | | |_) |
# |____/ \__,_|\__|\__|_|\___| |____/|_| |_|_| .__/
#                                            |_|

import random

class Game():
    def __init__(self):
        self.boardSize = 10
        self.playerShipBoard     = [["*" for i in range(self.boardSize)] for j in range(self.boardSize)]
        self.playerTargetBoard   = [["*" for i in range(self.boardSize)] for j in range(self.boardSize)]
        self.aiShipBoard         = [["*" for i in range(self.boardSize)] for j in range(self.boardSize)]
        self.aiTargetBoard       = [["*" for i in range(self.boardSize)] for j in range(self.boardSize)]

        self.playerShipCount = 0
        self.aiShipCount = 0
        self.playerHitCount  = 0
        self.aiHitCount      = 0
        self.playGame = True
        self.winner = ""

        # Ships = [['c','c','c','c','c'],['b','b','b','b'],['r','r','r'],['s','s','s'],['d','d']] #note

    def Intro(self):
        print("  ____        _   _   _        ____  _     _         ")
        print(" | __ )  __ _| |_| |_| | ___  / ___|| |__ (_)_ __    ")
        print(" |  _ \ / _` | __| __| |/ _ \ \___ \| '_ \| | '_ \   ")
        print(" | |_) | (_| | |_| |_| |  __/  ___) | | | | | |_) |  ")
        print(" |____/ \__,_|\__|\__|_|\___| |____/|_| |_|_| .__/   ")
        print("                                            |_|      ")
        print("         A Console Based Game of Death!              ")

    def getInput(self):

        return


    def validSpotPlayer(self, x, y): # checks if on board and water
        valid = False
        if x>=0 and x<self.boardSize and y<self.boardSize and self.playerShipBoard[x][y] not in ['c','b','r','s','d']:
            valid = True
        else:
            print("INVALID MOVE")
        return valid

    def validSpotAi(self, x, y): # checks if on board and water
        valid = False
        if x>=0 and x<self.boardSize and y<self.boardSize and self.aiShipBoard[x][y] not in ['c','b','r','s','d']:
            valid = True
        return valid

    def place(self, team, x, y, direction, letter):
        if team == "player":
            if letter == 'c' :
                if direction == 'n' and self.validSpotPlayer(x, y) and self.validSpotPlayer(x, y + 1)and self.validSpotPlayer(x, y + 2) and self.validSpotPlayer(x, y + 3) and self.validSpotPlayer(x, y + 4):
                    for i in range(0,5):
                        self.playerShipBoard[x][y+i] = letter
                elif direction == 's' and self.validSpotPlayer(x, y) and self.validSpotPlayer(x, y - 1)and self.validSpotPlayer(x, y - 2) and self.validSpotPlayer(x, y - 3) and self.validSpotPlayer(x, y - 4):
                    for i in range(0,5):
                        self.playerShipBoard[x][y-i] = letter
                elif direction == 'e' and self.validSpotPlayer(x, y) and self.validSpotPlayer(x + 1, y)and self.validSpotPlayer(x + 2, y) and self.validSpotPlayer(x + 3, y) and self.validSpotPlayer(x + 4, y):
                    for i in range(0,5):
                        self.playerShipBoard[x+i][y] = letter
                elif direction == 'w' and self.validSpotPlayer(x, y) and self.validSpotPlayer(x - 1, y)and self.validSpotPlayer(x - 2, y) and self.validSpotPlayer(x - 3, y) and self.validSpotPlayer(x - 4, y):
                    for i in range(0,5):
                        self.playerShipBoard[x-i][y] = letter
            elif letter == 'b':
                if direction == 'n' and self.validSpotPlayer(x, y) and self.validSpotPlayer(x, y + 1)and self.validSpotPlayer(x, y + 2) and self.validSpotPlayer(x, y + 3):
                    for i in range(0,4):
                        self.playerShipBoard[x][y+i] = letter
                elif direction == 's' and self.validSpotPlayer(x, y) and self.validSpotPlayer(x, y - 1)and self.validSpotPlayer(x, y - 2) and self.validSpotPlayer(x, y - 3):
                    for i in range(0,4):
                        self.playerShipBoard[x][y-i] = letter
                elif direction == 'e' and self.validSpotPlayer(x, y) and self.validSpotPlayer(x + 1, y)and self.validSpotPlayer(x + 2, y) and self.validSpotPlayer(x + 3, y):
                    for i in range(0,4):
                        self.playerShipBoard[x+i][y] = letter
                elif direction == 'w' and self.validSpotPlayer(x, y) and self.validSpotPlayer(x - 1, y)and self.validSpotPlayer(x - 2, y) and self.validSpotPlayer(x - 3, y):
                    for i in range(0,4):
                        self.playerShipBoard[x-i][y] = letter
            elif letter == 'r':
                if direction == 'n' and self.validSpotPlayer(x, y) and self.validSpotPlayer(x, y + 1)and self.validSpotPlayer(x, y + 2):
                    for i in range(0,3):
                        self.playerShipBoard[x][y+i] = letter
                elif direction == 's' and self.validSpotPlayer(x, y) and self.validSpotPlayer(x, y - 1)and self.validSpotPlayer(x, y - 2):
                    for i in range(0,3):
                        self.playerShipBoard[x][y-i] = letter
                elif direction == 'e' and self.validSpotPlayer(x, y) and self.validSpotPlayer(x + 1, y)and self.validSpotPlayer(x + 2, y):
                    for i in range(0,3):
                        self.playerShipBoard[x+i][y] = letter
                elif direction == 'w' and self.validSpotPlayer(x, y) and self.validSpotPlayer(x - 1, y)and self.validSpotPlayer(x - 2, y):
                    for i in range(0,3):
                        self.playerShipBoard[x-i][y] = letter
            elif letter == 's':
                if direction == 'n' and self.validSpotPlayer(x, y) and self.validSpotPlayer(x, y + 1)and self.validSpotPlayer(x, y + 2):
                    for i in range(0,3):
                        self.playerShipBoard[x][y+i] = letter
                elif direction == 's' and self.validSpotPlayer(x, y) and self.validSpotPlayer(x, y - 1)and self.validSpotPlayer(x, y - 2):
                    for i in range(0,3):
                        self.playerShipBoard[x][y-i] = letter
                elif direction == 'e' and self.validSpotPlayer(x, y) and self.validSpotPlayer(x + 1, y)and self.validSpotPlayer(x + 2, y):
                    for i in range(0,3):
                        self.playerShipBoard[x+i][y] = letter
                elif direction == 'w' and self.validSpotPlayer(x, y) and self.validSpotPlayer(x - 1, y)and self.validSpotPlayer(x - 2, y):
                    for i in range(0,3):
                        self.playerShipBoard[x-i][y] = letter
            elif letter == 'd':
                if direction == 'n' and self.validSpotPlayer(x, y) and self.validSpotPlayer(x, y + 1):
                    for i in range(0,2):
                        self.playerShipBoard[x][y+i] = letter
                elif direction == 's' and self.validSpotPlayer(x, y) and self.validSpotPlayer(x, y - 1):
                    for i in range(0,2):
                        self.playerShipBoard[x][y-i] = letter
                elif direction == 'e' and self.validSpotPlayer(x, y) and self.validSpotPlayer(x + 1, y):
                    for i in range(0,2):
                        self.playerShipBoard[x+i][y] = letter
                elif direction == 'w' and self.validSpotPlayer(x, y) and self.validSpotPlayer(x - 1, y):
                    for i in range(0,2):
                        self.playerShipBoard[x-i][y] = letter
        elif team == "ai":
            if letter == 'c' :
                if direction == 'n' and self.validSpotAi(x, y) and self.validSpotAi(x, y + 1)and self.validSpotAi(x, y + 2) and self.validSpotAi(x, y + 3) and self.validSpotAi(x, y + 4):
                    for i in range(0,5):
                        self.aiShipBoard[x][y+i] = letter
                elif direction == 's' and self.validSpotAi(x, y) and self.validSpotAi(x, y - 1)and self.validSpotAi(x, y - 2) and self.validSpotAi(x, y - 3) and self.validSpotAi(x, y - 4):
                    for i in range(0,5):
                        self.aiShipBoard[x][y-i] = letter
                elif direction == 'e' and self.validSpotAi(x, y) and self.validSpotAi(x + 1, y)and self.validSpotAi(x + 2, y) and self.validSpotAi(x + 3, y) and self.validSpotAi(x + 4, y):
                    for i in range(0,5):
                        self.aiShipBoard[x+i][y] = letter
                elif direction == 'w' and self.validSpotAi(x, y) and self.validSpotAi(x - 1, y)and self.validSpotAi(x - 2, y) and self.validSpotAi(x - 3, y) and self.validSpotAi(x - 4, y):
                    for i in range(0,5):
                        self.aiShipBoard[x-i][y] = letter
            elif letter == 'b':
                if direction == 'n' and self.validSpotAi(x, y) and self.validSpotAi(x, y + 1)and self.validSpotAi(x, y + 2) and self.validSpotAi(x, y + 3):
                    for i in range(0,4):
                        self.aiShipBoard[x][y+i] = letter
                elif direction == 's' and self.validSpotAi(x, y) and self.validSpotAi(x, y - 1)and self.validSpotAi(x, y - 2) and self.validSpotAi(x, y - 3):
                    for i in range(0,4):
                        self.aiShipBoard[x][y-i] = letter
                elif direction == 'e' and self.validSpotAi(x, y) and self.validSpotAi(x + 1, y)and self.validSpotAi(x + 2, y) and self.validSpotAi(x + 3, y):
                    for i in range(0,4):
                        self.aiShipBoard[x+i][y] = letter
                elif direction == 'w' and self.validSpotAi(x, y) and self.validSpotAi(x - 1, y)and self.validSpotAi(x - 2, y) and self.validSpotAi(x - 3, y):
                    for i in range(0,4):
                        self.aiShipBoard[x-i][y] = letter
            elif letter == 'r':
                if direction == 'n' and self.validSpotAi(x, y) and self.validSpotAi(x, y + 1)and self.validSpotAi(x, y + 2):
                    for i in range(0,3):
                        self.aiShipBoard[x][y+i] = letter
                elif direction == 's' and self.validSpotAi(x, y) and self.validSpotAi(x, y - 1)and self.validSpotAi(x, y - 2):
                    for i in range(0,3):
                        self.aiShipBoard[x][y-i] = letter
                elif direction == 'e' and self.validSpotAi(x, y) and self.validSpotAi(x + 1, y)and self.validSpotAi(x + 2, y):
                    for i in range(0,3):
                        self.aiShipBoard[x+i][y] = letter
                elif direction == 'w' and self.validSpotAi(x, y) and self.validSpotAi(x - 1, y)and self.validSpotAi(x - 2, y):
                    for i in range(0,3):
                        self.aiShipBoard[x-i][y] = letter
            elif letter == 's':
                if direction == 'n' and self.validSpotAi(x, y) and self.validSpotAi(x, y + 1)and self.validSpotAi(x, y + 2):
                    for i in range(0,3):
                        self.aiShipBoard[x][y+i] = letter
                elif direction == 's' and self.validSpotAi(x, y) and self.validSpotAi(x, y - 1)and self.validSpotAi(x, y - 2):
                    for i in range(0,3):
                        self.aiShipBoard[x][y-i] = letter
                elif direction == 'e' and self.validSpotAi(x, y) and self.validSpotAi(x + 1, y)and self.validSpotAi(x + 2, y):
                    for i in range(0,3):
                        self.aiShipBoard[x+i][y] = letter
                elif direction == 'w' and self.validSpotAi(x, y) and self.validSpotAi(x - 1, y)and self.validSpotAi(x - 2, y):
                    for i in range(0,3):
                        self.aiShipBoard[x-i][y] = letter
            elif letter == 'd':
                if direction == 'n' and self.validSpotAi(x, y) and self.validSpotAi(x, y + 1):
                    for i in range(0,3):
                        self.aiShipBoard[x][y+i] = letter
                elif direction == 's' and self.validSpotAi(x, y) and self.validSpotAi(x, y - 1):
                    for i in range(0,3):
                        self.aiShipBoard[x][y-i] = letter
                elif direction == 'e' and self.validSpotAi(x, y) and self.validSpotAi(x + 1, y):
                    for i in range(0,3):
                        self.aiShipBoard[x+i][y] = letter
                elif direction == 'w' and self.validSpotAi(x, y) and self.validSpotAi(x - 1, y):
                    for i in range(0,3):
                        self.aiShipBoard[x-i][y] = letter
        return

    def fire(self,team,x,y):
        if team == "player":
            if x>=0 and x<self.boardSize and y>=0 and y<self.boardSize and self.aiShipBoard[x][y] in ('c', 'b', 'r', 's', 'd') : # hit
                self.playerHitCount          += 1
                self.playerTargetBoard[x][y] = 'X'
                self.aiShipBoard[x][y]       = 'X'
            elif self.validSpotPlayer(x, y):                                # miss
                self.playerTargetBoard[x][y] = '@'
                self.aiShipBoard[x][y]       = '@'
        elif team == "ai":
            if x>=0 and x<self.boardSize and y>=0 and y<self.boardSize and self.playerShipBoard[x][y] in ('c', 'b', 'r', 's', 'd') : # hit
                self.aiHitCount              += 1
                self.aiTargetBoard[x][y]     = 'X'
                self.playerShipBoard[x][y]   = 'X'
            elif self.validSpotPlayer(x, y):                                    # miss
                self.playerTargetBoard[x][y] = '@'
                self.aiShipBoard[x][y]       = '@'
            return

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



game = Game()
game.Intro()

# set up player
game.place("player", 0, 0, 'e', 'c')
game.place("player", 0, 1, 'e', 'd')
game.place("player", 0, 2, 'e', 's')
game.place("player", 0, 3, 'e', 'r')
game.place("player", 0, 4, 'e', 'b')

#set up AI
game.place("ai", 0, 0, 'e', 'c')
game.place("ai", 0, 1, 'e', 'd')
game.place("ai", 0, 2, 'e', 's')
game.place("ai", 0, 3, 'e', 'r')
game.place("ai", 0, 4, 'e', 'b')



while(game.playGame):
    # print("Place your ships\nShips = [['c','c','c','c','c'],['b','b','b','b'],['r','r','r'],['s','s','s'],['d','d']]")
    # game.draw("player")
    # print("Enter an x, y coordinate (0-9),a direction, and a ship letter")
    # while(!game.playerShipsplaced):
    #     x = int(input("Enter x: "))
    #     y = int(input("Enter y: "))
    #     d = input("Enter dir: ")
    #     L = input("Enter Ship Letter: ")
    #     game.place("player", x , y, d, L)
    #     game.draw("player")

    print("Fire at x,y")
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    game.fire("player",x,y)
    game.draw("player")

    x = random.randint(0,10)
    y = random.randint(0,10)
    game.fire("ai",x,y)
    game.draw("player")












