#  ____        _   _   _        ____  _     _
# | __ )  __ _| |_| |_| | ___  / ___|| |__ (_)_ __
# |  _ \ / _` | __| __| |/ _ \ \___ \| '_ \| | '_ \
# | |_) | (_| | |_| |_| |  __/  ___) | | | | | |_) |
# |____/ \__,_|\__|\__|_|\___| |____/|_| |_|_| .__/
#                                            |_|
class Game():
    def __init__(self):
        self.boardSize = 10
        self.playerShipBoard     = [["*" for i in range(self.boardSize)] for j in range(self.boardSize)]
        self.playerTargetBoard   = [["*" for i in range(self.boardSize)] for j in range(self.boardSize)]
        self.aiShipBoard         = [["*" for i in range(self.boardSize)] for j in range(self.boardSize)]
        self.aiTargetBoard       = [["*" for i in range(self.boardSize)] for j in range(self.boardSize)]

        self.playerHitCount  = 0
        self.aiHitCount      = 0
        self.playGame = True
        self.winner = ""

        # Ships = [['c','c','c','c','c'],['b','b','b','b'],['r','r','r'],['s','s','s'],['d','d']] #note

    def validSpot(self, x, y): # only checks if on board
        valid = False
        if x>=0 and x<=self.boardSize and y<=self.boardSize:
            valid = True
        return valid

    def place(self, team, x, y, direction, letter):
        if team == "player":
            if letter == 'c' :
                if direction == 'n' and self.validSpot(x,y) and self.validSpot(x,y+1)and self.validSpot(x,y+2) and self.validSpot(x,y+3) and self.validSpot(x,y+4):
                    for i in range(0,5):
                        self.playerShipBoard[x][y+i] = letter
                elif direction == 's' and self.validSpot(x,y) and self.validSpot(x,y-1)and self.validSpot(x,y-2) and self.validSpot(x,y-3) and self.validSpot(x,y-4):
                    for i in range(0,5):
                        self.playerShipBoard[x][y-i] = letter
                elif direction == 'e' and self.validSpot(x,y) and self.validSpot(x+1,y)and self.validSpot(x+2,y) and self.validSpot(x+3,y) and self.validSpot(x+4,y):
                    for i in range(0,5):
                        self.playerShipBoard[x+i][y] = letter
                elif direction == 'w' and self.validSpot(x,y) and self.validSpot(x-1,y)and self.validSpot(x-2,y) and self.validSpot(x-3,y) and self.validSpot(x-4,y):
                    for i in range(0,5):
                        self.playerShipBoard[x-i][y] = letter
            elif letter == 'b':
                if direction == 'n' and self.validSpot(x,y) and self.validSpot(x,y+1)and self.validSpot(x,y+2) and self.validSpot(x,y+3):
                    for i in range(0,4):
                        self.playerShipBoard[x][y+i] = letter
                elif direction == 's' and self.validSpot(x,y) and self.validSpot(x,y-1)and self.validSpot(x,y-2) and self.validSpot(x,y-3):
                    for i in range(0,4):
                        self.playerShipBoard[x][y-i] = letter
                elif direction == 'e' and self.validSpot(x,y) and self.validSpot(x+1,y)and self.validSpot(x+2,y) and self.validSpot(x+3,y):
                    for i in range(0,4):
                        self.playerShipBoard[x+i][y] = letter
                elif direction == 'w' and self.validSpot(x,y) and self.validSpot(x-1,y)and self.validSpot(x-2,y) and self.validSpot(x-3,y):
                    for i in range(0,4):
                        self.playerShipBoard[x-i][y] = letter
            elif letter == 'r':
                if direction == 'n' and self.validSpot(x,y) and self.validSpot(x,y+1)and self.validSpot(x,y+2):
                    for i in range(0,3):
                        self.playerShipBoard[x][y+i] = letter
                elif direction == 's' and self.validSpot(x,y) and self.validSpot(x,y-1)and self.validSpot(x,y-2):
                    for i in range(0,3):
                        self.playerShipBoard[x][y-i] = letter
                elif direction == 'e' and self.validSpot(x,y) and self.validSpot(x+1,y)and self.validSpot(x+2,y):
                    for i in range(0,3):
                        self.playerShipBoard[x+i][y] = letter
                elif direction == 'w' and self.validSpot(x,y) and self.validSpot(x-1,y)and self.validSpot(x-2,y):
                    for i in range(0,3):
                        self.playerShipBoard[x-i][y] = letter
            elif letter == 's':
                if direction == 'n' and self.validSpot(x,y) and self.validSpot(x,y+1)and self.validSpot(x,y+2):
                    for i in range(0,3):
                        self.playerShipBoard[x][y+i] = letter
                elif direction == 's' and self.validSpot(x,y) and self.validSpot(x,y-1)and self.validSpot(x,y-2):
                    for i in range(0,3):
                        self.playerShipBoard[x][y-i] = letter
                elif direction == 'e' and self.validSpot(x,y) and self.validSpot(x+1,y)and self.validSpot(x+2,y):
                    for i in range(0,3):
                        self.playerShipBoard[x+i][y] = letter
                elif direction == 'w' and self.validSpot(x,y) and self.validSpot(x-1,y)and self.validSpot(x-2,y):
                    for i in range(0,3):
                        self.playerShipBoard[x-i][y] = letter
            elif letter == 'd':
                if direction == 'n' and self.validSpot(x,y) and self.validSpot(x,y+1):
                    for i in range(0,2):
                        self.playerShipBoard[x][y+i] = letter
                elif direction == 's' and self.validSpot(x,y) and self.validSpot(x,y-1):
                    for i in range(0,2):
                        self.playerShipBoard[x][y-i] = letter
                elif direction == 'e' and self.validSpot(x,y) and self.validSpot(x+1,y):
                    for i in range(0,2):
                        self.playerShipBoard[x+i][y] = letter
                elif direction == 'w' and self.validSpot(x,y) and self.validSpot(x-1,y):
                    for i in range(0,2):
                        self.playerShipBoard[x-i][y] = letter
        elif team == "ai":
            if letter == 'c' :
                if direction == 'n' and self.validSpot(x,y) and self.validSpot(x,y+1)and self.validSpot(x,y+2) and self.validSpot(x,y+3) and self.validSpot(x,y+4):
                    for i in range(0,5):
                        self.aiShipBoard[x][y+i] = letter
                elif direction == 's' and self.validSpot(x,y) and self.validSpot(x,y-1)and self.validSpot(x,y-2) and self.validSpot(x,y-3) and self.validSpot(x,y-4):
                    for i in range(0,5):
                        self.aiShipBoard[x][y-i] = letter
                elif direction == 'e' and self.validSpot(x,y) and self.validSpot(x+1,y)and self.validSpot(x+2,y) and self.validSpot(x+3,y) and self.validSpot(x+4,y):
                    for i in range(0,5):
                        self.aiShipBoard[x+i][y] = letter
                elif direction == 'w' and self.validSpot(x,y) and self.validSpot(x-1,y)and self.validSpot(x-2,y) and self.validSpot(x-3,y) and self.validSpot(x-4,y):
                    for i in range(0,5):
                        self.aiShipBoard[x-i][y] = letter
            elif letter == 'b':
                if direction == 'n' and self.validSpot(x,y) and self.validSpot(x,y+1)and self.validSpot(x,y+2) and self.validSpot(x,y+3):
                    for i in range(0,4):
                        self.aiShipBoard[x][y+i] = letter
                elif direction == 's' and self.validSpot(x,y) and self.validSpot(x,y-1)and self.validSpot(x,y-2) and self.validSpot(x,y-3):
                    for i in range(0,4):
                        self.aiShipBoard[x][y-i] = letter
                elif direction == 'e' and self.validSpot(x,y) and self.validSpot(x+1,y)and self.validSpot(x+2,y) and self.validSpot(x+3,y):
                    for i in range(0,4):
                        self.aiShipBoard[x+i][y] = letter
                elif direction == 'w' and self.validSpot(x,y) and self.validSpot(x-1,y)and self.validSpot(x-2,y) and self.validSpot(x-3,y):
                    for i in range(0,4):
                        self.aiShipBoard[x-i][y] = letter
            elif letter == 'r':
                if direction == 'n' and self.validSpot(x,y) and self.validSpot(x,y+1)and self.validSpot(x,y+2):
                    for i in range(0,3):
                        self.aiShipBoard[x][y+i] = letter
                elif direction == 's' and self.validSpot(x,y) and self.validSpot(x,y-1)and self.validSpot(x,y-2):
                    for i in range(0,3):
                        self.aiShipBoard[x][y-i] = letter
                elif direction == 'e' and self.validSpot(x,y) and self.validSpot(x+1,y)and self.validSpot(x+2,y):
                    for i in range(0,3):
                        self.aiShipBoard[x+i][y] = letter
                elif direction == 'w' and self.validSpot(x,y) and self.validSpot(x-1,y)and self.validSpot(x-2,y):
                    for i in range(0,3):
                        self.aiShipBoard[x-i][y] = letter
            elif letter == 's':
                if direction == 'n' and self.validSpot(x,y) and self.validSpot(x,y+1)and self.validSpot(x,y+2):
                    for i in range(0,3):
                        self.aiShipBoard[x][y+i] = letter
                elif direction == 's' and self.validSpot(x,y) and self.validSpot(x,y-1)and self.validSpot(x,y-2):
                    for i in range(0,3):
                        self.aiShipBoard[x][y-i] = letter
                elif direction == 'e' and self.validSpot(x,y) and self.validSpot(x+1,y)and self.validSpot(x+2,y):
                    for i in range(0,3):
                        self.aiShipBoard[x+i][y] = letter
                elif direction == 'w' and self.validSpot(x,y) and self.validSpot(x-1,y)and self.validSpot(x-2,y):
                    for i in range(0,3):
                        self.aiShipBoard[x-i][y] = letter
            elif letter == 'd':
                if direction == 'n' and self.validSpot(x,y) and self.validSpot(x,y+1):
                    for i in range(0,3):
                        self.aiShipBoard[x][y+i] = letter
                elif direction == 's' and self.validSpot(x,y) and self.validSpot(x,y-1):
                    for i in range(0,3):
                        self.aiShipBoard[x][y-i] = letter
                elif direction == 'e' and self.validSpot(x,y) and self.validSpot(x+1,y):
                    for i in range(0,3):
                        self.aiShipBoard[x+i][y] = letter
                elif direction == 'w' and self.validSpot(x,y) and self.validSpot(x-1,y):
                    for i in range(0,3):
                        self.aiShipBoard[x-i][y] = letter
        return

    def fire(self,team,x,y):
        if team == "player":
            if self.validSpot(x,y) and self.aiShipBoard[x][y] in ('c','b','r','s','d') : # hit
                self.playerHitCount          += 1
                self.playerTargetBoard[x][y] = 'X'
                self.aiShipBoard[x][y]       = 'X'
            elif self.validSpot(x,y):                                # miss
                self.playerTargetBoard[x][y] = '@'
                self.aiShipBoard[x][y]       = '@'
        elif team == "ai":
            if self.validSpot(x,y) and self.playerShipBoard[x][y] in ('c','b','r','s','d') : # hit
                self.aiHitCount              += 1
                self.aiTargetBoard[x][y]     = 'X'
                self.playerShipBoard[x][y]   = 'X'
            elif self.validSpot(x,y):                                    # miss
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
# game.draw("player")
game.place("player", 0, 0, 'e', 'd')
# game.draw("player")
# game.draw("ai")
# game.fire("ai",0,0)
# game.draw("player")
# game.draw("ai")
game.fire("player",0,0)
game.draw("player")
game.draw("ai")











