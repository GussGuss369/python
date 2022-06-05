user = int(input("Enter an integer greater that 1: "))
product = 1
factor = 0
while product < user:
    factor += 1
    product = product * factor
    
if user == product:
    product = 1
    for n in range(1, (factor + 1)):
        product = product * n
        print(n)
else:
    print("No result")