total = 0
count = 1
n1 , n2 = 0 , 1

user = int(input("enter the nth term you want: "))
if user < 0:
    print("enter a positive intiger")
elif user == 1 or user == 0:
    print(n1)
else:
    while count < user: 
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
print(n1)