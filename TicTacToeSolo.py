class Board:
    theBoard = {'TOPL' : ' ', 'TOPM' : ' ', 'TOPR' : ' ',
                'MIDL' : ' ', 'MIDM' : ' ', 'MIDR' : ' ',
                'BOTL' : ' ', 'BOTM' : ' ', 'BOTR' : ' '}
                
    def printBoard(self, board):
        print(board['TOPL']+'|'+board['TOPM']+'|'+board['TOPR'])
        print('-+-+-')
        print(board['MIDL']+'|'+board['MIDM']+'|'+board['MIDR'])
        print('-+-+-')
        print(board['BOTL']+'|'+board['BOTM']+'|'+board['BOTR'])

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

gameLogic = logic()
display = Board()
turn = 'X'
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