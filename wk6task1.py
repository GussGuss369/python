from re import L


def displayMenu():
    print("1. input datat and save to new file")
    print("2. Input data and append to existing file")
    print("3. Calculate and display average mark")
    print("4. Display data")
    print("5. Quit")
    choice = int(input("Enter your choice: "))
    while choice > 5 or choice < 1:
        choice = int(input("Enter choice again: "))
    return choice

def saveToFile(openMode):
    studentRecord = []
    try:
        testResultFile = open("studentNamesfile.txt", openMode)
        studentMark = "0"
        studentName = input("Enter a name, xxx to finish: ")
        while studentName != "xxx":
            studentMark = input("Enter mark: ")
            studentRecord.append([studentName,studentMark])
            testResultFile.write(studentName + "," + studentMark + "\n")
            studentName = input("Enter a name, xxx to finish: ")
        testResultFile.close()
    except:
        print("Error in write to file")

def calculateAverage():
    studentMark = []
    try:
        testResultFile = open("studentNamesfile.txt", "r")
        total = 0
        numRecs = 0
        for line in testResultFile: 
            mark=int(line.split(",")[1])
            studentMark.append(mark)
            total += mark           
            numRecs += 1
        testResultFile.close()
        average = total / numRecs
        print(f"average mark: {average}")
    except:
        print("Error in average")

def displayData():
    studentMark = []
    try:
        testResultFile = open("studentNamesfile.txt", "r")
        for line in testResultFile: 
            print(line)
        testResultFile.close()
    except:
        print("Error in displayData")


option = displayMenu()
while option != 5:
    if option == 1:
        saveToFile("w")
    elif option == 2:
        saveToFile("a")
    elif option == 3:
        calculateAverage()
    elif option == 4:
        displayData()
    else:
        print("Error in menu")
    option = displayMenu()
print("You have chosen to quit the program")