import random as ran, time

class Board:
    theBoard = {'TOPL' : ' ', 'TOPM' : ' ', 'TOPR' : ' ',
                'MIDL' : ' ', 'MIDM' : ' ', 'MIDR' : ' ',
                'BOTL' : ' ', 'BOTM' : ' ', 'BOTR' : ' '}
    
    listBoard = [[' ', ' ', ' '],[' ',' ',' '],[' ',' ',' ']]
                
    def printBoard(self, board):
        print(board['TOPL']+'|'+board['TOPM']+'|'+board['TOPR'])
        print('-+-+-')
        print(board['MIDL']+'|'+board['MIDM']+'|'+board['MIDR'])
        print('-+-+-')
        print(board['BOTL']+'|'+board['BOTM']+'|'+board['BOTR'])

    def updateList(self,board,arr):
        countX = 0
        countY = 0
        for val in board.values():
            if countY == len(arr[countX]):
                countX += 1
                countY = 0
            arr[countX][countY] = val
            countY += 1  


            
class logic:
    def __init__(self):
        print("Legend: Top, Mid, or Bot and (L)eft, (R)ight, or (M)iddle")
        print("Example: 'TopL' for Top left or 'MidM' for Centre")

    def takeTurn(self, board, who):
        print('Turn for ' + who + '. Move on which space?')
        move  = input().upper()
        if move in board.keys() and board[move] == ' ':
            board[move] = who
        else:
            print("Invalid move, try again...")
            self.takeTurn(board,who)

    def checkVictory(self, board):
        if(board['TOPL'] == board['TOPM'] == board['TOPR'] != ' ') or (board['TOPL'] == board['MIDM'] == board['BOTR'] != ' ') or (board['TOPL'] == board['MIDL'] == board['BOTL'] != ' '):
            print(board['TOPL'] +" has won!")
            return True
        if(board['TOPR'] == board['MIDM'] == board['BOTL'] != ' ') or (board['TOPR'] == board['MIDR'] == board['BOTR'] != ' '):
            print(board['TOPR'] +" has won!")
            return True
        if(board['MIDL'] == board['MIDM'] == board['MIDR'] != ' ') or (board['TOPM'] == board['MIDM'] == board['BOTM'] != ' '):
            print(board['MIDM'] +" has won!")
            return True
        if(board['BOTL'] == board['BOTM'] == board['BOTR'] != ' '):
            print(board['BOTL'] +" has won!")
            return True

class AI:
    prevTurn = [-1,-1,-1]

    listDictConversion = [["TOPL","TOPM","TOPR"],["MIDL","MIDM","MIDR"],["BOTL","BOTM", "BOTR"]]


    def takeTurn(self,board,boardArr,conversionArr, first, lastTurn):
        if first:
            search = True
            while search:
                X = ran.randint(0,2)
                Y = ran.randint(0,2)
                if boardArr[Y][X] == ' ':
                    board[conversionArr[Y][X]] = 'O'
                    lastTurn = [Y,X,ran.randint(1,2)]
                    search = False
        else:
            if board['MIDM'] == 'O':
                search = True
                switch = 0
                while search and switch != 2:
                    if lastTurn[2] == 1:
                        if board['TOPL'] == ' ':
                            board['TOPL'] = 'O'
                            lastTurn = [0,0,1]
                            search = False
                        elif board['BOTR'] == ' ':
                            board['BOTR'] = 'O'
                            lastTurn = [2,2,1]
                            search = False
                        else: 
                            lastTurn[2] = 2
                            switch += 1 
                    else:
                        if board['TOPR'] == ' ':
                            board['TOPR'] = 'O'
                            lastTurn = [0,2,2]
                            search = False
                        elif board['BOTL'] == ' ':
                            board['BOTL'] = 'O'
                            lastTurn = [2,0,2]
                            search = False
                        else:
                            lastTurn[2] = 1
                            switch += 1

            elif (boardArr[lastTurn[0]-1][lastTurn[1]] == ' ' or boardArr[(lastTurn[0]+1)%3][lastTurn[1]] == ' ') and lastTurn[2] == 1 and not (boardArr[lastTurn[0]-1][lastTurn[1]] == 'X' and boardArr[(lastTurn[0]+1)%3][lastTurn[1]] == 'X'):
                if boardArr[lastTurn[0]-1][lastTurn[1]] == ' ':
                    board[conversionArr[lastTurn[0]-1][lastTurn[1]]] = 'O'
                    lastTurn = [lastTurn[0]-1,lastTurn[1],1]
                else:
                    board[conversionArr[(lastTurn[0]+1)%3][lastTurn[1]]] = 'O'
                    lastTurn = [(lastTurn[0]+1)%3,lastTurn[1],1]
            elif (boardArr[lastTurn[0]][lastTurn[1]-1] == ' ' or boardArr[lastTurn[0]][(lastTurn[1]+1)%3] == ' ') and lastTurn[2] == 2 and not (boardArr[lastTurn[0]][lastTurn[1]-1] == 'X' and boardArr[lastTurn[0]][(lastTurn[1]+1)%3] == 'X'):
                if boardArr[lastTurn[0]][lastTurn[1]-1] == ' ':
                    board[conversionArr[lastTurn[0]][lastTurn[1]-1]] = 'O'
                    lastTurn = [lastTurn[0],lastTurn[1]-1,2]
                else:
                    board[conversionArr[lastTurn[0]][(lastTurn[1]+1)%3]] = 'O'
                    lastTurn = [lastTurn[0],(lastTurn[1]+1)%3,2]
        lastTurn = listNegConv(lastTurn)
        return lastTurn


    def checkWinRow(self,arr,forWin,forAgainst):
        flag = 0
        check = -1
        for countY in range(len(arr)):
            for countX in range(len(arr[countY])):
                if arr[countY][countX] == forWin:
                    flag += 1
                if arr[countY][countX] == forAgainst:
                    flag -= 1
            if flag == 2:
                check = countY
                break
            flag = 0
        return check

    def checkWinCol(self,arr,forWin,forAgainst):
        flag = 0
        col = 0
        check = -1 
        for countX in range(len(arr[col])):
            for countY in  range(len(arr)):
                if arr[countY][countX] == forWin:
                    flag += 1
                if arr[countY][countX] == forAgainst:
                    flag -= 1
            if flag == 2:
                check = countX
                break
            flag = 0
            col += 1 % 3
        return check
    
    def checkWinDiag(self,arr,forWin,forAgainst):
        if arr[1][1] == forWin:
            if arr[0][0] == forWin and arr[2][2] == ' ':
                return 1
            elif arr[0][2] == forWin and arr[2][0] == ' ':
                return 2
            elif arr[2][0] == forWin and arr[0][2]:
                return 3
            elif arr[2][2] == forWin and arr[0][0]:
                return 4
        elif ((arr[0][0] == forWin and arr[2][2] == forWin ) or (arr[0][2] == forWin and arr[2][0] == forWin)) and arr[1][1] != forAgainst:
            return 5
        return -1
    
    def placeRow(self,board,arr,row):
        for col in range(len(arr[row])):
            if arr[row][col] in board.keys() and board[arr[row][col]] == ' ':
                board[arr[row][col]] = 'O'
                break
    
    def placeCol(self,board,arr,col):
        for row in range(len(arr)):
            if arr[row][col] in board.keys() and board[arr[row][col]] == ' ':
                board[arr[row][col]] = 'O'
                break
    
    def placeDiag(self,board,state):
        if state == 1 and board['BOTR'] == ' ':
            board['BOTR'] = 'O'
        elif state == 2 and board['BOTL'] == ' ':
            board['BOTL'] = 'O'
        elif state == 3 and board['TOPR'] == ' ':
            board['TOPR'] = 'O'
        elif state == 4 and board['TOPL'] == ' ':
            board['TOPL'] = 'O'
        elif board['MIDM'] == ' ':
            board['MIDM'] = 'O'

def listNegConv(arr):
    for i in range(len(arr)):
        if arr[i] <0:
            arr[i] = 2
    return arr


turn = 'X'
playAgainst = 'a'
while playAgainst != 'Y' and playAgainst != 'N':
    print("Would you like to play against an AI? Y/N")
    playAgainst = input().upper()
    if playAgainst != 'Y' and playAgainst != 'N':
        print("Error: Please input Y for yes or N for no...")
gameLogic = logic()
display = Board()

if playAgainst == 'Y':
    bot = AI()
    TurnOne = True
    for i in range(9):
        if i%2 == 0:
            display.printBoard(display.theBoard)
            gameLogic.takeTurn(display.theBoard, turn)

        if i%2 == 1:
            if bot.checkWinRow(display.listBoard,'X','O') != -1 and (bot.checkWinCol(display.listBoard,'O','X') == -1 and bot.checkWinRow(display.listBoard,'O','X') == -1):
                bot.placeRow(display.theBoard,bot.listDictConversion,bot.checkWinRow(display.listBoard, 'X','O'))
            elif bot.checkWinCol(display.listBoard,'X','O') != -1 and (bot.checkWinCol(display.listBoard,'O','X') == -1 and bot.checkWinRow(display.listBoard,'O','X') == -1):
                bot.placeCol(display.theBoard,bot.listDictConversion,bot.checkWinCol(display.listBoard, 'X','O'))
            elif bot.checkWinDiag(display.listBoard,'X','O') != -1 and (bot.checkWinCol(display.listBoard,'O','X') == -1 and bot.checkWinRow(display.listBoard,'O','X') == -1):
                bot.placeDiag(display.theBoard,bot.checkWinDiag(display.listBoard,'X','O'))
            else:
                if bot.checkWinRow(display.listBoard,'O','X') != -1:
                    bot.placeRow(display.theBoard,bot.listDictConversion,bot.checkWinRow(display.listBoard, 'O','X'))
                elif bot.checkWinCol(display.listBoard,'O','X') != -1:
                    bot.placeCol(display.theBoard,bot.listDictConversion,bot.checkWinCol(display.listBoard, 'O','X'))
                elif bot.checkWinDiag(display.listBoard,'O','X') != -1:
                    bot.placeDiag(display.theBoard,bot.checkWinDiag(display.listBoard,'O','X'))
                else:
                    bot.prevTurn = bot.takeTurn(display.theBoard,display.listBoard,bot.listDictConversion,TurnOne,bot.prevTurn)
                    TurnOne = False
                
        if gameLogic.checkVictory(display.theBoard) == True:
            break
        if i == 8:
            print("Tie! Thank you for playing.")
        display.updateList(display.theBoard,display.listBoard)
    display.printBoard(display.theBoard)

                

else:
    for i in range(9):
        display.printBoard(display.theBoard)
        gameLogic.takeTurn(display.theBoard, turn)
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        if gameLogic.checkVictory(display.theBoard) == True:
            break
    display.printBoard(display.theBoard)
