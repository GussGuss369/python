names = ["Belinda", "Gerri", "Tom"]
for i in range(0,6):
    try:
        print(names[i])
    except:
        print("No more names in the array!")
    
print("Program continuing")

age = ""
while isinstance(age,str):
    try:
        age = input("enter age: ")
        age = int(age)
    except:
        print("please enter an integer")
    