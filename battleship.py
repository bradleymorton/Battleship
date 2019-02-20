


class Game():
    def __init__(self):
        baordSize = 10
        playerShipBoard     = [['*']*boardSize, ['*']*boardSize]
        playerTargetBoard   = [['*']*boardSize, ['*']*boardSize]
        aiShipBoard         = [['*']*boardSize, ['*']*boardSize]
        aiTargetBoard       = [['*']*boardSize, ['*']*boardSize]

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
            playerShipBoard[x][y] = letter
        if team == "ai":
            aiShipBoard[[x], [y]] = letter

        return

    def fire(self,team,x,y):
        if team == "player":
            if validSpot(x,y) and aiShipBoard[x][y] == letter: # hit
                playerHitCount          += 1
                playerTargetBoard[x][y] = 'X'
                aiShipbaord[x][y]       = 'X'
            else if validSpot(x,y):
                playerTargetBoard[x][y] = '@'
                aiShipbaord[x][y]       = '@'
        if team == "ai":
            if validSpot(x,y) and playerShipBoard[x][y] == letter: # hit
                aiHitCount              += 1
                aiTargetBoard[x][y]     = 'X'
                playerShipbaord[x][y]   = 'X'
            else if validSpot(x,y)
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


def draw(self):
    return














