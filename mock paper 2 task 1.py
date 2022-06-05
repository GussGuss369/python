NumberIn = int(input("Enter a positive whole number: "))
NumberOut = 0
count = 0

while NumberIn > 0:
    count = count + 1
    PartValue = NumberIn % 2
    NumberIn = NumberIn // 2 
    for i in range(1, (count)):
        PartValue = PartValue * 10
    NumberOut = NumberOut + PartValue

print(f"The result is: {NumberOut}")
