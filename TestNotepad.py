def getInput(file):
    while True:
        note = input("Please add your notes:\n")
        note +="\n"
        file.write(note)
        optionTwo = input("Are you done? Y\\N \n")
        if optionTwo == "Y":
            print("Notes saved!")
            break

filename = input("Please enter the name file you want to open: ")
filename += ".txt"
fileAlreadyExists = False
option = "E"
optionTwo = ""

try:
    readFile = open(filename, "r")
    fileAlreadyExists = True
except:
    readFile = open(filename, "w+")

readFile.close()

if (fileAlreadyExists):
    option = input("Please select your action\n"
                   "A) Read The File.\nB) Override The File and Start Over.\n"
                   "C) Append Your Current Work.\n"
                   "D) Replace a Line.\n"
                   "E) Exit\n")
else:
    readFile = open(filename,"w")
    print("You created a new file named", filename, end="\n")
    getInput(readFile)
    readFile.close()

while option != "E":
    if option == "A":
        readFile = open(filename, "r")
        for line in readFile:
            print(line)
        readFile.close()
    elif option == "B":
        readFile = open(filename, "w")
        print(filename, "is overridden. A fresh start for all of us!\n")
        getInput(readFile)
        readFile.close()
    elif option == "C":
        readFile = open(filename, "a")
        print(filename,"is ready for adding new notes!")
        getInput(readFile)
        readFile.close()
    elif option == "D":
        counter = 0
        readFile = open(filename, "r")
        linesArray = []
        for line in readFile:
            linesArray.append(line)
        readFile.close()
        readFile = open(filename, "r")
        for line in readFile:
            print(counter+1, line)
            counter +=1
        readFile.close()
        counter = int(input("Please pick the line you want to replace: "))-1
        newText = input("Please write the new text: \n")
        newText += "\n"
        linesArray[counter] = newText
        readFile = open(filename,"w+")
        for line in linesArray:
            readFile.write(line)
    option = input("Please select your action\n"
                   "A) Read The File.\nB) Override The File and Start Over.\n"
                   "C) Append Your Current Work.\n"
                   "D) Replace a Line.\n"
                   "E) Exit\n")



