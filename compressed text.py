user = input("enter the text: ")
count = 1
COMPRESSED = ""

for i in range(0, len(user)-1): 
        current = user[i]
        if current == user[i+1]:
            count += 1 
        else:
            count = 1
            print(user[i], str(count))