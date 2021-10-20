def FizzBuzz(x):
  for num in range(1, x + 1):
    if num % 3 == 0 and num % 5 == 0:
      print("FizzBuzz")
    elif num % 3 == 0:
      print("Fizz")
    elif num % 5 == 0:
      print("Buzz")
    else:
      print(num)
user = int(input("enter the range you would like: "))      
FizzBuzz(user)