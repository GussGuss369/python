def new_func():
    userx = int(input("enter the x coordinate: "))
    usery = int(input("enter the y coordinate: "))
    strr = "y = -6x + 4"
    if strr[4].isdigit() == True:
        will_hit = ((int(strr[4]) * userx) + int(strr[9]))
    elif strr[4].isdigit() == False:
        will_hit = ((int(strr[5]) * userx) + int(strr[9]))
    if will_hit == usery:
        print("True")
    else: 
        print("False")

new_func()


def new_func():
    count = 0
    userx = int(input("enter the x coordinate: "))
    usery = int(input("enter the y coordinate: "))
    strr = "y = -6x + 4"
    for i in strr:
        count += 1
        if count.isdigit() == True:
            will_hit = ((int(strr[4]) * userx) + int(strr[9]))
        elif count.isdigit() == False:
            pass 
        if will_hit == usery:
            print("True")
        else:   
            print("False")

new_func()
