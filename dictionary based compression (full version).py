sentence = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY"
word = input("enter a word to find in the sentence: ")

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
    line_list = stripped_line. split()
    list_of_lists. append(line_list)
    a_file
print(list_of_lists)