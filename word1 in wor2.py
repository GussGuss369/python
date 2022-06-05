count = 0
count2 = 0
word1 = str(input("enter the first word: "))
word2 = str(input("enter the second word: "))

lst1 = list(word1)
lst2 = list(word2)
if len(word1) <= len(word2):
    for i in word1.split():
        count += 1
        for j in word2.split():
            count2 += 1
            if i == j:
                print("TRUE")
            else:
                print("FALSE")
else:
    print("the second word is shorter than the first word")


print("SIR VERSION")

word1 = "EAT"
word2 = "ATE"

list1 = list(word1)
list2 = list(word2)

counts1 = {}

for letter in list1:
    if letter in counts1:
        counts1[letter] = counts1[letter] + 1
    else:
        counts1[letter] = 1

counts2 = {}
for letter in list2:
    if letter in counts2:
        counts2[letter] = counts2[letter] + 1
    else:
        counts2[letter] = 1

formed = True
for key,value in counts1.items():
    try:
        if (counts2.get(key) < counts1.get(key)):
            formed = False
            break
    except:
        print(word1, "can not be formed from", word2)
        exit()
        
if formed == True:
    print(word1, "can be formed from", word2)
else:
    print(word1, "can not be formed from", word2)