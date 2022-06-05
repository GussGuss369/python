user = input("enter word: ")
word = []
for i in user:
    word += i
count = 0
word = word[::-1]
print(word) 
for i in word:
    if i == "a":
        word[count] = "0"
    elif i == "e":
        word[count] = "1"
    elif i == "i":
        word[count] = "2"
    elif i == "o":
        word[count] = "2"
    elif i == "u":
        word[count] = "3"
    count += 1
print(word)