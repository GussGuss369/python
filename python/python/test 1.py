#excercise 1)a)b)c):
food = input("enter your favorite food: ")
color = input("enter your favorite color: ")
food1 = (f"my favorite food is {food}...")
color1 = (f"my favorite color is {color}...")
answer = food1 + "" + color1
print(answer)
print("my favorite food is",food,"... and my favorite color is",color,"...")
print(f"my favorite food is {food.upper()}... and my favorite color is {color.upper()}")

#excercise 2)a):
division = 40 // 11
print(division)
#b) 
remainder = 40 % 11
print(remainder)
#c)
calculate = 2**10
print(calculate)
#d)
if 1 <= 4 and 7 <= 7:
  print("True")
else:
  print("false")

#excercise 3):
import datetime
hour = float(input("enter the number of hours you require: "))
time_now = datetime.datetime.now()
print(time_now.strftime("Time now: %A %d %B %Y %H:%M:%S"))
time_change = datetime.timedelta(hours=(hour))
expiry = datetime.datetime.now() + time_change
print(f"Expires: {expiry}") 
if hour == 2:
  print("charge: £3.50")
elif hour == 3 or hour == 4:
  print("charge: £5.00")
elif hour > 4 and hour <= 12:
  print("charge: £10.00")
else:
  print("Invalid input")

#excercise 4):
def multiply(x, y):
    if y < 0:
        return -multiply(x, -y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply(x, y - 1)
print(multiply(1378, 871));
#OR
total = 0
for i in range(871):
    total = total + 1378
print(total)

#excercise 5):
from random import randint
number = randint(1,10)
number_of_guesses = 1
print("Guess a number between 1 and 10")
guess = int(input())
while guess != number:
  print("Incorrect")
  number_of_guesses = number_of_guesses + 1
  print("Guess a number between 1 and 10")
  guess = int(input())
print("Well done!")
print(f"you have guessed {number_of_guesses} time(s) until you have reached the correct answer")