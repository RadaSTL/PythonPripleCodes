import sys
from termcolor import colored, cprint

def CreateBoard(arr):
    for i in range(0,8):
        arr.append(["⬤","⬤","⬤","⬤","⬤","⬤"])

def DrawBoard(arr):
    linecount = 1
    for i in range(5, -1, -1):
        if i == 5: print("  ① ② ⓷ ⓸ ⓹ ⓺ ⓻")
        for j in range(0, 7):
            if j == 0:
                print(linecount, end=" ")
                linecount += 1
            print(arr[j][i], end=" ")
        print("")

def addPoint(board, column, playNumber):
    if playNumber == 1:
        circle = colored("⬤", "blue")
    if playNumber == 2:
        circle = colored("⬤", "red")
    row = 0
    while True:
        try:
            if board[column][row] == "⬤":
                board[column][row] = circle
                return True
            else:
                row += 1
        except:
            print("Please try another column.")
            return False

def winCheck (boardArr, playNumber):
    wincount = 0
    if playNumber == 1:
        circle = colored("⬤", "blue")
    if playNumber == 2:
        circle = colored("⬤", "red")
    #Horizontal win check
    for i in range(len(boardArr)):
        for j in range(len(boardArr[i])):
            if wincount >= 4:
                print(playNumber, "has won!")
                return True
            if boardArr[i][j] == circle:
                wincount += 1
            else:
                wincount = 0

    #Vertical win check
    colCursor = 0
    while colCursor <= 5:
        for i in range(len(boardArr)):
            if wincount >= 4:
                print("Player",playNumber, "has won!")
                return True
            if boardArr[i][colCursor] == circle:
                wincount += 1
            else:
                wincount = 0
        colCursor += 1

    # Diagonal Increasing
    colCursor = 0
    while colCursor <= 5:
        diagCursor = 0
        for i in range(len(boardArr)):
            if wincount >= 4:
                print("Player",playNumber, "has won!")
                return True
            if colCursor + diagCursor < 6:
                if boardArr[i][colCursor+diagCursor] == circle:
                    wincount += 1
            else:
                wincount = 0
            diagCursor += 1
        colCursor += 1

    # Diagonal Decrease
    colCursor = 0
    while colCursor <= 5:
        diagCursor = 0
        for i in range(len(boardArr)):
            if wincount >= 4:
                print("Player",playNumber, "has won!")
                return True
            if colCursor - diagCursor > -1:
                if boardArr[i][colCursor-diagCursor] == circle:
                    wincount += 1
            else:
                wincount = 0
            diagCursor += 1
        colCursor += 1

    return False




BoardArray = []
CreateBoard(BoardArray)

playerNum = 2
while True:
    if playerNum == 2:
        playerNum = 1
    else:
        playerNum = 2
    DrawBoard(BoardArray)
    playText = "Player " +  str(playerNum) + " please pick a column: "
    pickedCol = int(input(playText))-1
    boolPick = addPoint(BoardArray,pickedCol,playerNum)
    while boolPick == False:
        pickedCol = int(input(playText))
        boolPick = addPoint(BoardArray, pickedCol, playerNum)
    if winCheck(BoardArray, playerNum):
        DrawBoard(BoardArray)
        break







