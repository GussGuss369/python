count1 = 0
count2 = 0
number = int(input("enter a numebr: "))
if number <= 1:
    print("Not greater than one")
elif number > 1:
    for i in range(2, number):
        if number % i == 0:
            count1 += 1
        else:
            count2 += 1

if count1 > 0:
    print("Is not prime")
else:
    print("Is prime") 