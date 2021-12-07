#marwan version
number = input("enter a number: ")
string = "digits are is: "

for i in number:
    string = string + " " + i

print(string) 

#SIR VERSION:
number = input("enter a number: ")
x = number // 100
number = number % 100
y = number // 10
number = number % 10
z = number

print(f"the digits are {x}, {y}, {z}")