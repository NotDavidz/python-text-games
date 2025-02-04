#2025
import random

choice = str.upper(input("Enter: \t \"A\" for 1 player \n\t \"B\" for 2 Players \n\t \"Other\" for Exit: " ))
turn = "Player 1"
symbol = True
board = [["", "1", "2", "3"], ["A", "", "", ""], ["B", "", "", ""], ["C", "", "", ""]]
choice_vector = ["",""]

def printBoard():

    for x in range(0, 4):
        print(board[x][0] + "\t" + board[x][1] + "\t" + board[x][2] + "\t" + board[x][3])

def reset():
    global turn, symbol, board
    turn = "Player 1"
    symbol = True
    board = [["", "1", "2", "3"], ["A", "", "", ""], ["B", "", "", ""], ["C", "", "", ""]]

def updateBoard(x, y, text_symbol, updateRole):
    global turn, symbol
    if board[x][y] != "":
        return True
    board[x][y] = text_symbol
    if updateRole and not checkWinCon() and not checkFull():
        symbol = not symbol
        if (turn == "Player 2" or turn == "bot"):
            turn = "Player 1"
        elif (turn == "Player 1" and choice == "B"):
            turn = "Player 2"
        else:
            turn = "bot"

def conv():
    global choice_vector
    if choice_vector[1] != "1" and choice_vector[1] != "2" and choice_vector[1] != "3":
        return False
    if choice_vector[0] != "A" and choice_vector[0] != "B" and choice_vector[0] != "C":
        return False
    
    if choice_vector[0] == "A":
        choice_vector = [1, choice_vector[1]]
        return True
    elif choice_vector[0] == "B":
        choice_vector = [2, choice_vector[1]]
        return True   
    elif choice_vector[0] == "C":
        choice_vector = [3, choice_vector[1]]
        return True
    return False

def players():
    global choice_vector
    printBoard()
    choice_vector = str.upper(input("This is " + turn + "'s turn, enter a coordinate \"Letter,Number\": ")).split(",",1)
    if conv():
        if updateBoard(int(choice_vector[0]),int(choice_vector[1]), "O" if symbol else "X", True):
            print("Spot Taken, try another")
    else:
        print("Invalid Position, try another")

def botAlg():
    ran = random.randrange(1,6,1)
    while (ran > 0):
        for i in range (1,4):
            for j in range (1,4):
                if board[i][j] == "": 
                    if ran == 0:
                        updateBoard(i, j, "O" if symbol else "X", True)
                        return
                    else:
                        ran-=1
    

        

def bot():
    global choice_vector
    printBoard()
    if turn == ("Player 1"):
        choice_vector = str.upper(input("This is your turn, enter a coordinate \"Letter,Number\": ")).split(",",1)
        if conv():
            if updateBoard(int(choice_vector[0]),int(choice_vector[1]), "O" if symbol else "X", True):
                print("Spot Taken, try another")
        else:
            print("Invalid Position, try another")
    else:
        print("The bot has made it's move")
        botAlg()

def checkWinCon():
    diagonal = False
    diagonal = (board[1][1] == board [2][2] == board [3][3] != "") or (board[3][1] == board [2][2] == board [1][3] != "")
    if diagonal:
        return True
    for i in range(1,4):
        if board[i][1] ==  board[i][2] ==  board[i][3] != "":
            return True
        if board[1][i] ==  board[2][i] ==  board[3][i] != "":
            return True
    return False

def checkFull():
    for i in range(0,4):
        for j in range(0,4):
            if board[i][j] == "" and i != 0:
                return False
    return True


while (choice == "A" or choice == "B"):
    print("___________________ \n PLAYER TURN: "+turn)
    if (choice == "B"):
        players()
    if (choice == "A"):
        bot()
    if checkFull():
        printBoard()
        choice = str.upper(input("Game Tied! \n Enter: \t \"A\" for 1 player \n\t\t \"B\" for 2 Players \n\t\t \"Other\" for Exit: "))
        reset()
    elif checkWinCon():
        printBoard()
        choice = str.upper(input(turn + " has won the game! \nEnter: \t \"A\" for 1 player \n\t \"B\" for 2 Players \n\t \"Other\" for Exit: "))
        reset()
    


print("Thanks for playing!") 



