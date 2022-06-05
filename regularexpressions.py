import re
myString = "aab"
expression = "[a]+[b]+"
re.match(expression, myString)
result = bool(re.match(expression, myString))
print(result)

print("new one")

expression = "[b]+[a]+"
re.match(expression, myString)
result = bool(re.match(expression, myString))
print(result)

print("new one")

user = (input("enter the string: "))
myString = (user)
expression = "^[bc]*[a]$"
re.match(expression, myString)
result = bool(re.match(expression, myString))
print(result)

print("new one")

liststr = ["a" , "bcaa", "bca", "bcbca", "bcabca"]
expression = "^[bc]*[a]$"
for i in liststr:
    result = bool(re.match(expression, i))
    print(result)