import random
board=['-','-','-',
       '-','-','-',
       '-','-','-']
winner=None
gamerunning=True
current_player='X'
def printBoard():
    print(board[0]+' | '+board[1]+' | '+board[2])
    print('_________')
    print(board[3]+' | '+board[4]+' | '+board[5])
    print('_________')
    print(board[6]+' | '+board[7]+' | '+board[8])
# def userInput():
#     # inp=input('choose between O or X :')
#     num=int(input('choose position number to insert O or X:'))
#     return inp,num
def put_player_move(inp,num,board):
    if num in range(1,10) and board[num-1]=='-':
        board[num-1]=inp
    else:
        print('oops!! the place is already marked')
def winRow(board):
    global winner
    for i in range(0,7):
        if board[i]==board[i+1]==board[i+2] !='-':
            winner=board[i]
            return True
        i+=3
def winColumn(board):
    global winner
    for i in range(0,3):
        if board[i]==board[i+3]==board[i+6] !='-':
            winner=board[i]
            return True
        i+=1
def winDiagonal(board):
    global winner
    if board[0]==board[4]==board[8]  and board[0]!='-' :
        winner=board[0]
        return True
    elif board[2]==board[4]==board[6] and board[2]!='-' :
        winner=board[2]
        return True
def winCheck():
    global winner
    global gamerunning
    if winRow(board) or winColumn(board) or winDiagonal(board):
        printBoard()
        print(f"The winner is {winner}")
        gamerunning=False
        # exit() SUCH HARD EXITS ARE PROHIBITED
def Tiecheck():
    global gamerunning
    # if '-' not in board:
    if not(winRow(board)) and not(winColumn(board)) and not(winDiagonal(board)) and '-' not in board:
        printBoard()
        print('IT IS A TIE!!')
        gamerunning=False 
def switch_player():
    global current_player
    if current_player=='X':
        current_player='O'
    else:
        current_player='X'

def computer(board):
    while current_player == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switch_player()
while gamerunning:
    printBoard()
    num=int(input('choose position number to insert O or X:'))
    put_player_move(current_player,num,board)
    # printBoard()
    winCheck()
    Tiecheck()
    switch_player()
    computer(board)
    winCheck()
    Tiecheck()
    
# HEY I'M GLAD TO PUBLISH MY FIRST SIMPLE GAME OF TIC TAC TOE. YIPEEE!!! INITIALLY I HAD DONE WITH A PLAYER RANDOMLY PUTTING 
# O OR X . SO ADDED A SWITCH PLAYER FUNCTION  BUT BETTER WITH COMPUTER RATHER THAN BETWWEN MY LEFT AND RIGHT HAND 




