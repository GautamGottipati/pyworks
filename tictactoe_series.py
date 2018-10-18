import random

def drawBoard(board):
    print(' '+board[7]+'|'+board[8]+'|'+board[9])
    print('-------')
    print(' '+board[4]+'|'+board[5]+'|'+board[6])
    print('-------')
    print(' '+board[1]+'|'+board[2]+'|'+board[3])

def inputPlayerLetter():
    letter=''
    while not(letter=="X" or letter=="O"):
        print("Do you want to be X or O?")
        letter=input().upper()
    if letter=='X':
        return ['X','O']
    else:
        return ['O','X']

def isSpaceFree(board,move):
    return board[move].isdigit()

def makeMove(board,letter,move):
    if isSpaceFree(board,move):
        board[move]=letter
    else:
        raise Exception("Make move:The field is not empty")

def getPlayerMove(board):
    move=''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,int(move)):
        print("What is your next move? Select number b/w (1-9)")
        move=input()
    return int(move)

def whoGoesFirst():
    if random.randint(0,1)==0:
        return 'computer'
    else:
        return 'player'

def getComputerMove(board,computerLetter):
    if computerLetter=="X":
        playerLetter="O"
    else:
        playerLetter="X"

    #first check if we can win in next move
    for i in range(1,10):
        copy=getBoardCopy(board)
        if isSpaceFree(copy,i):
            makeMove(copy,computerLetter,i)
            if isWinner(copy,computerLetter):
                return i
    #check if player can win in the next move
    for i in range(1,10):
        copy=getBoardCopy(board)
        if isSpaceFree(copy,i):
            makeMove(copy,playerLetter,i)
            if isWinner(copy,playerLetter):
                return i
    #take one of corner if they are free
    move=chooseRandomMoveFromList(board,[1,3,7,9])
    if move !=None:
        return move
    #center move on board
    if isSpaceFree(board,5):
        return 5
    #move on one of the sides
    return chooseRandomMoveFromList(board,[2,4,6,8])
        
            

def getBoardCopy(board):
    dupeBoard=[]
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def chooseRandomMoveFromList(board,moveList):
    possibleMoves=[]
    for i in moveList:
        if isSpaceFree(board,i):
            possibleMoves.append(i)

    if len(possibleMoves)>0:
        return random.choice(possibleMoves)
    else:
        return None
    
def isWinner(bo,le):
    return ((bo[7]==le and bo[8]==le and bo[9]==le)or
            (bo[4]==le and bo[5]==le and bo[6]==le)or
            (bo[1]==le and bo[2]==le and bo[3]==le)or
            (bo[7]==le and bo[4]==le and bo[1]==le)or
            (bo[8]==le and bo[5]==le and bo[2]==le)or
            (bo[9]==le and bo[6]==le and bo[3]==le)or
            (bo[7]==le and bo[5]==le and bo[3]==le)or
            (bo[9]==le and bo[5]==le and bo[1]==le))

def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False
    return True

def main():
    print("Welcome to Tic Tac Toe!")
    x=int(input("How many matches would you like to play\t"))
    totalMatches=x
    com_score=0
    player_score=0
    random.seed()
    #x=1
    print("---------Start Game------------")
    while x:
        #reset the board
        theBoard=['']*10

        for i in range(9,0,-1):
            theBoard[i]=str(i)
        drawBoard(theBoard)
        playerLetter,computerLetter=inputPlayerLetter()
        turn=whoGoesFirst()
        print("The "+turn+" will go first")

        gameIsPlaying=True
        while gameIsPlaying:
            if turn=="player":
                #player turn
                drawBoard(theBoard)
                move=getPlayerMove(theBoard)
                makeMove(theBoard,playerLetter,move)
                if isWinner(theBoard,playerLetter):
                    drawBoard(theBoard)
                    print("Congratulation winner")
                    player_score+=1
                    gameIsPlaying=False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print("D   R   A   W")
                        com_score+=1
                        player_score+=1
                        
                        break
                    else:
                        turn="computer"
                
            else:
                move=getComputerMove(theBoard,computerLetter)
                makeMove(theBoard,computerLetter,move)
                if isWinner(theBoard,computerLetter):
                    drawBoard(theBoard)
                    print("The computer wins and you Loose")
                    com_score+=1
                    gameIsPlaying=False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print("D   R   A   W")
                        com_score+=1
                        player_score+=1
                        break
                    else:
                        turn="player"
        
        x-=1
        if(x):
            print("\n------------Game number "+str(totalMatches-x+1)+"---------")
    print("======================================")
    print("Thankyou for playing")
    if(com_score>player_score):
        print("Computer has won the series")
    elif(com_score<player_score):
        print("Hurray! you won the series")
    elif(com_score==player_score):
        print("Series draw")
    else:
        print("You need to play atleast 1 match")
    print("Your points     :"+str(player_score)+"/"+str(totalMatches))
    print("Computers score :"+str(com_score)+"/"+str(totalMatches))
                
                
        

if __name__=="__main__":
    main()

            
            
