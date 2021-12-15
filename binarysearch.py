names = ["Alan", " Bob","Carl", "Dave", "Ed", "Fred", "Gerl", "Hal", "Jo", "Ken", "Lara", "Mo", "Nedm", "Pam"]
def binarySearch(itemSearched):
    counter = 0
    start = 0
    end = len(names) - 1
    found = False
    while found == False:
        middle = (start + end)//2
        if end < start:
            return False
        if itemSearched == names[middle]:
            found = True
        elif itemSearched < names[middle]:
            end = middle - 1
        elif itemSearched > names[middle]:
            start = middle + 1
            counter += 1
    return found

user = input("enter a name to find from the list")
print(binarySearch(user))