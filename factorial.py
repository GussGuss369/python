user = int(input("enter a number: "))
count = 0
total = 1
for i in range(user):
    total = (user - count) * total
    count += 1
print(total)

def factorial(x):
    if x == 0:
        return 1
    else:
        return (x * factorial(x-1))

print(factorial(user))