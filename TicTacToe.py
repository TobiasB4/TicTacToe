theBoard = {'TOPL' : ' ', 'TOPM' : ' ', 'TOPR' : ' ',
            'MIDL' : ' ', 'MIDM' : ' ', 'MIDR' : ' ',
            'BOTL' : ' ', 'BOTM' : ' ', 'BOTR' : ' '}

def printBoard(board):
    print(board['TOPL']+'|'+board['TOPM']+'|'+board['TOPR'])
    print('-+-+-')
    print(board['MIDL']+'|'+board['MIDM']+'|'+board['MIDR'])
    print('-+-+-')
    print(board['BOTL']+'|'+board['BOTM']+'|'+board['BOTR'])

def takeTurn(board, who):
    print('Turn for ' + turn + '. Move on which space?')
    move  = input().upper()
    if move in board.keys() and board[move] == ' ':
        board[move] = who
    else:
        print("Invalid move, try again...")
        takeTurn(board,who)

def checkVictory(board):
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

print("Legend: Top, Mid, or Bot and (L)eft, (R)ight, or (M)iddle")
print("Example: 'TopL' for Top left or 'MidM' for Centre")

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    takeTurn(theBoard, turn)
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    if checkVictory(theBoard) == True:
        break
printBoard(theBoard)