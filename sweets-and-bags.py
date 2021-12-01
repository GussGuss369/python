bag = int(input("enter an integer number for the number of bags: "))
sweets = int(input("enter an integer number for the number of sweets: "))
if sweets > bag:
    if sweets // bag != 0:
        print("it is possible")
        new_bag = bag + 1
        for i in (str(new_bag)):
            total = sweets % bag
            print(f"There would be {total} sweet(s) in the first bag")
            bag = bag - 1
            for i in (str(bag)):
                new_total = sweets - total
                new_new_total = sweets // bag
                print(f"there would be {new_new_total} sweet(s) in the marginal bag")
    elif sweets == bag:
        print("it is possible")
    else:
        print("it is impossible")
elif sweets == bag:
    print("you cannot have equal sweets and bags")
else:
    print("it is impossible as sweets are less thean the number of bags")