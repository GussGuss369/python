sentence = "askaskaskaskask country"
word = input("enter a word to find in the sentence: ")
user = input("enter the sentece to compress: ")

f = open("sentence" , "w")
f.write(user)
f.close()

user = input("enter the sentece to compress: ")

f = open("sentence" , "w")
f.write(user)
f.close()

f = open("sentence" , "w")
print(f.read())

def task1(sentence, word):
    s = sentence.lower().split()
    positions = []
    found = False
    for i in range(0, len(s)):
        if word.lower() == s[i]:
            found = True
            positions.append(i+1)
       
    return positions if found else "Word not found"

print(task1(sentence, word))

a_file = open("sentence", "r")
list_of_lists = []
for line in a_file:
    stripped_line = line. strip()
    line_list = stripped_line.split()
    list_of_lists. append(line_list)
    a_file
print(list_of_lists)

b_file = open("sentence" , "r")
for string in b_file:
    new_string = string.replace("ask","1")
    new_string = string.replace("not","2")
    new_string = string.replace("ask","3")
    new_string = string.replace("ask","4")
    new_string = string.replace("ask","5")
    new_string = string.replace("ask","6")
    new_string = string.replace("ask","7")
    new_string = string.replace("ask","8")
    new_string = string.replace("ask","9")
    
print(b_file.read())
b_file.close()