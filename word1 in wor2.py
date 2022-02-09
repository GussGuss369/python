count = 0
count2 = 0
word1 = str(input("enter the first word: "))
word2 = str(input("enter the second word: "))

lst1 = list(word1)
lst2 = list(word2)
for i in word1.split():
    count += 1
    for j in word2.split():
        count2 += 1
        if i == j:
            print("TRUE")
        else:
            print("FALSE")

