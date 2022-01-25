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

def task2(sentence):
    unique_words = []
    positions = []
    for word in sentence.split():
        if word not in unique_words:
            unique_words.append(word)
    for word in sentence.split():
        for u in range(len(unique_words)):
            if unique_words[u] == word:
                positions.append(u+1)

    try:
        with open("sentence", "w") as f:
            f.write(str(positions))
    except:
        print("Error with file")

    
    return unique_words, positions


print(task2(sentence))