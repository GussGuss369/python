n = ["Anna", "Jon", "Paul"]
counter = 0
found = False
user = input("enter a name")
while counter < len(n):
    if n[counter] == user:
        found = True
        print(counter)
    counter += 1 

if found == False:
    print(-1)