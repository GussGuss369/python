slow = 0
meduim = 0
fast = 0
loop = True
while loop:
    user = int(input("enter the data: "))
    if user == 0:
        print(f"fast people = {fast}, meduim people = {meduim}, slow people = {slow}")
        break;
    if user < 30:
        fast += 1
    elif user < 60:
        meduim += 1
    elif user > 60:
        slow += 1