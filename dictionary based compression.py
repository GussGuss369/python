statement = input("enter the statement: ").lower()
word = input("enter the word you would want to check for repetition: ").lower()
counter = 0
nstatement = statement.split()
index = 0
if word in statement:
    for i in range(0, len(nstatement)):
        index = index + 1
        if word == nstatement[i]:
            counter = counter + 1
            print(f"the word ask in in position {index}")

else:
    print("Error. The word is not in the sentece")

print(f"the word {word} repeats {counter} time(s)")