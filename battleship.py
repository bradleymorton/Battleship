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

        self.playerShipPlaced = 0
        self.aiShipPlaced = 0

        self.playerFireList = []
        self.aiFireList = []

        self.playerHitCount= 0
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


    def validSpotPlayer(self, x, y): # checks if on board and water
        valid = False
        if x>=0 and x<self.boardSize and y<self.boardSize and self.playerShipBoard[x][y] not in ['c','b','r','s','d']:
            valid = True
        else:
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
                    for i in range(0,3):
                        self.aiShipBoard[x][y+i] = letter
                    return True
                elif direction == 'n' and self.validPlacementAi(x, y) and self.validPlacementAi(x, y - 1):
                    for i in range(0,3):
                        self.aiShipBoard[x][y-i] = letter
                    return True
                elif direction == 'e' and self.validPlacementAi(x, y) and self.validPlacementAi(x + 1, y):
                    for i in range(0,3):
                        self.aiShipBoard[x+i][y] = letter
                    return True
                elif direction == 'w' and self.validPlacementAi(x, y) and self.validPlacementAi(x - 1, y):
                    for i in range(0,3):
                        self.aiShipBoard[x-i][y] = letter
                    return True
        return False

    def fire(self,team,x,y):
        if team == "player":
            if x>=0 and x<self.boardSize and y>=0 and y<self.boardSize and self.aiShipBoard[x][y] in ('c', 'b', 'r', 's', 'd') : # hit
                self.aiHitCount          += 1
                self.playerTargetBoard[x][y] = 'X'
                self.aiShipBoard[x][y]       = 'X'
                self.playerFireList.append([x,y])
            elif self.validSpotAi(x, y):                                # miss
                self.playerTargetBoard[x][y] = '@'
                self.aiShipBoard[x][y]       = '@'
                self.playerFireList.append([x, y])
        elif team == "ai":
            if x>=0 and x<self.boardSize and y>=0 and y<self.boardSize and self.playerShipBoard[x][y] in ('c', 'b', 'r', 's', 'd') : # hit
                self.playerHitCount              += 1
                self.aiTargetBoard[x][y]     = 'X'
                self.playerShipBoard[x][y]   = 'X'
                self.aiFireList.append([x, y])
            elif self.validSpotPlayer(x, y):                                    # miss
                self.playerShipBoard[x][y] = '@'
                self.aiTargetBoard[x][y]       = '@'
                self.aiFireList.append([x, y])

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

#HARD CODE SET
# set up player
# game.place("player", 0, 0, 'e', 'c')
# game.place("player", 0, 1, 'e', 'd')
# game.place("player", 0, 2, 'e', 's')
# game.place("player", 0, 3, 'e', 'r')
# game.place("player", 0, 4, 'e', 'b')
#
# #set up AI
# game.place("ai", 0, 0, 'e', 'c')
# game.place("ai", 0, 1, 'e', 'd')
# game.place("ai", 0, 2, 'e', 's')
# game.place("ai", 0, 3, 'e', 'r')
# game.place("ai", 0, 4, 'e', 'b')



while(game.playGame):
    print("Place your ships\nShips = [['c','c','c','c','c'],['b','b','b','b'],['r','r','r'],['s','s','s'],['d','d']]")
    game.draw("player")

    # check direction and replace

    print("Enter an x, y coordinate (0-9),and direction (n,s,e,w)")

    # Place player ships
    while(game.playerShipPlaced < 5):

        print("place Cruiser")
        while(True):
            x = int(input("Enter x: "))
            if x<0 or x>=game.boardSize:
                print("try again")
                x = int(input("Enter x: "))

            y = int(input("Enter y: "))
            if y < 0 or y >= game.boardSize:
                print("try again")
                y = int(input("Enter y: "))

            while(True):
                d = input("Enter dir: ")
                if d not in ['n','s','e','w']:
                    continue
                else:
                    break

            L = 'c'
            if game.place("player",x,y,d,L):
                game.place("player", x , y, d, L)
                game.playerShipPlaced += 1
                game.draw("player")
                break;
            else:
                print("can't place ship here")
                continue

        print("Place Battleship")
        while (True):
            x = int(input("Enter x: "))
            if x < 0 or x >= game.boardSize:
                print("try again")
                x = int(input("Enter x: "))

            y = int(input("Enter y: "))
            if y < 0 or y >= game.boardSize:
                print("try again")
                y = int(input("Enter y: "))

            while (True):
                d = input("Enter dir: ")
                if d not in ['n', 's', 'e', 'w']:
                    continue
                else:
                    break;

            L = 'b'

            if game.place("player",x,y,d,L):
                game.place("player", x, y, d, L)
                game.draw("player")
                game.playerShipPlaced += 1
                break
            else:
                print("can't place ship here")
                continue

        print("Place Carrier")
        while(True):
            x = int(input("Enter x: "))
            if x<0 or x>=game.boardSize:
                print("try again")
                x = int(input("Enter x: "))

            y = int(input("Enter y: "))
            if y < 0 or y >= game.boardSize:
                print("try again")
                y = int(input("Enter y: "))

            while(True):
                d = input("Enter dir: ")
                if d not in ['n','s','e','w']:
                    continue
                else:
                    break;

            L = 'r'

            if game.validPlacementPlayer(x, y):
                game.place("player", x , y, d, L)
                game.playerShipPlaced += 1
                game.draw("player")
                break
            else:
                print("cant place ship here")
                continue

        print("Place Sub")
        while (True):
            x = int(input("Enter x: "))
            if x < 0 or x >= game.boardSize:
                print("try again")
                x = int(input("Enter x: "))

            y = int(input("Enter y: "))
            if y < 0 or y >= game.boardSize:
                print("try again")
                y = int(input("Enter y: "))

            while (True):
                d = input("Enter dir: ")
                if d not in ['n', 's', 'e', 'w']:
                    continue
                else:
                    break;

            L = 's'

            if game.validPlacementPlayer(x, y):
                game.place("player", x, y, d, L)
                game.playerShipPlaced += 1
                game.draw("player")
                break
            else:
                print("cant place ship here")
                continue

        print("Place Destroyer")
        while (True):
            x = int(input("Enter x: "))
            if x < 0 or x >= game.boardSize:
                print("try again")
                x = int(input("Enter x: "))

            y = int(input("Enter y: "))
            if y < 0 or y >= game.boardSize:
                print("try again")
                y = int(input("Enter y: "))

            while (True):
                d = input("Enter dir: ")
                if d not in ['n', 's', 'e', 'w']:
                    continue
                else:
                    break;

            L = 'd'

            if game.validPlacementPlayer(x,y):
                game.place("player", x, y, d, L)
                game.playerShipPlaced += 1
                game.draw("player")
                break
            else:
                print("cant place ship here")
                continue

        # Place ai ships
        direction=['n', 's', 'e', 'w']
        while (game.playerShipPlaced < 5):

            while (True):
                x = random.randint(0,10)
                y = random.randint(0,10)
                direction = random.randint(0,5)
                d=directions[direction]
                L = 'c'
                if game.place("ai", x, y, d, L):
                    game.place("ai", x, y, d, L)
                    game.aiShipPlaced += 1
                    break
                else:
                    continue

            while (True):
                x = random.randint(0,10)
                y = random.randint(0,10)
                direction = random.randint(0,5)
                d=directions[direction]
                L = 'b'
                if game.place("ai", x, y, d, L):
                    game.place("ai", x, y, d, L)
                    game.aiShipPlaced += 1
                    break
                else:
                    continue

            while (True):
                x = random.randint(0,10)
                y = random.randint(0,10)
                direction = random.randint(0,5)
                d=directions[direction]
                L = 'r'
                if game.place("ai", x, y, d, L):
                    game.place("ai", x, y, d, L)
                    game.aiShipPlaced += 1
                    break
                else:
                    continue

            while (True):
                x = random.randint(0,10)
                y = random.randint(0,10)
                direction = random.randint(0,5)
                d=directions[direction]
                L = 's'
                if game.place("ai", x, y, d, L):
                    game.place("ai", x, y, d, L)
                    game.aiShipPlaced += 1
                    break
                else:
                    continue

            while (True):
                x = random.randint(0,10)
                y = random.randint(0,10)
                direction = random.randint(0,5)
                d=directions[direction]
                L = 'd'
                if game.place("ai", x, y, d, L):
                    game.place("ai", x, y, d, L)
                    game.aiShipPlaced += 1
                    break
                else:
                    continue


    game.draw("ai")

    #FIRE
    while(True):

        # player fire
        print("Fire at x,y")
        x = int(input("Enter x: "))
        if x<0 or x>=game.boardSize:
            print("try again")
            x = int(input("Enter x: "))
        y = int(input("Enter y: "))
        if y < 0 or y >= game.boardSize:
            print("try again")
            y = int(input("Enter y: "))
        if [x,y] in game.playerFireList:
            print("you already fired there")
            continue

        game.fire("player",x,y)
        game.draw("player")
        game.checkWin()
        if game.playGame == False:
            break

        # ai fire
        x = random.randint(0,10)
        y = random.randint(0,10)
        game.fire("ai",x,y)
        game.draw("player")

print()
print(game.winner)










