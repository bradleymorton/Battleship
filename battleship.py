


class Game():
    def __init__(self):
        boardSize = 10
        board = [['*']*boardSize, ['*']*boardSize]
        playerShipBoard     = board
        playerTargetBoard   = board
        aiShipBoard         = board
        aiTargetBoard       = board

        playerHitCount  = 0
        aiHitCount      = 0
        playGame = True
        winner = ""
        playerShips = [['c','c','c','c','c'],['b','b','b','b'],['r','r','r'],['s','s','s'],['d','d']] #fix later
        aiShips     = [['c','c','c','c','c'],['b','b','b','b'],['r','r','r'],['s','s','s'],['d','d']]

    def validSpot(self,x,y): # only checks if on board
        validSpot = False
        if x>=0 and x<=10 and y>=0 and y<=10:
            validSpot = True
        return True

    def place(self,team,x,y,direction,letter):
        if team == "player":
            if letter == 'c' :
                if direction == 'n' and validSpot(x,y) and validSpot(x,y+1)and validSpot(x,y+2) and validSpot(x,y+3) and validSpot(x,y+4):
                    for i in range(0,5):
                     playerShipBoard[x][y+i] = letter
                elif direction == 's' and validSpot(x,y) and validSpot(x,y-1)and validSpot(x,y-2) and validSpot(x,y-3) and validSpot(x,y-4):
                    for i in range(0,5):
                     playerShipBoard[x][y-i] = letter
                elif direction == 'e' and validSpot(x,y) and validSpot(x+1,y)and validSpot(x+2,y) and validSpot(x+3,y) and validSpot(x+4,y):
                    for i in range(0,5):
                     playerShipBoard[x+i][y] = letter
                elif direction == 'w' and validSpot(x,y) and validSpot(x-1,y)and validSpot(x-2,y) and validSpot(x-3,y) and validSpot(x-4,y):
                    for i in range(0,5):
                     playerShipBoard[x-i][y] = letter
            # elif letter == 'b' :
            # elif letter == 'r' :
            # elif letter == 's' :
            # elif letter == 'd' :
                return

    def fire(self,team,x,y):
        if team == "player":
            if validSpot(x,y) and aiShipBoard[x][y] == letter : # hit     FIX!!!!!!
                playerHitCount          += 1
                playerTargetBoard[x][y] = 'X'
                aiShipbaord[x][y]       = 'X'
            elif validSpot(x,y):                                # miss
                playerTargetBoard[x][y] = '@'
                aiShipbaord[x][y]       = '@'
        if team == "ai":
            if validSpot(x,y) and playerShipBoard[x][y] == letter : # hit   FIX!!!!!!!!
                aiHitCount              += 1
                aiTargetBoard[x][y]     = 'X'
                playerShipboard[x][y]   = 'X'
            elif validSpot(x,y):                                    # miss
                playerTargetBoard[x][y] = '@'
                aiShipbaord[x][y]       = '@'
            return

    def checkWin(self):
        if playerHitCount == 17:
            playGame = False
            winner = "AI WINS!"
        if aiHitCount == 17:
            playGame = False
            winner = "PLAYER WINS!"
        return


def draw(self, team):
    if team == player:
        print("This is the target board")
        for x in range(boardSize):
            for y in range(boardSize):
                print(playerTargetBoard[x][y])
            print("\n")
        print("This is your board")
        for x in range(boardSize):
            for y in range(boardSize):
                print(playerShipBoard[x][y])
            print("\n")
    return


    return














