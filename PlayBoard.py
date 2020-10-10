def playBoardCreate(rows,columns):
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            if j%2==0:
                if j != columns:
                    print(" ", end="")
                else:
                    print(" ")
            else:
                if j != columns:
                    print("|", end="")
                else:
                    print("|")
        print("-"*columns)
    if (rows > 6 or columns > 109):
        return False
    else:
        return True

playBoardCreate(6,109)