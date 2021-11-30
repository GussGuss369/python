sentence = input("input your sentence: ")
count = 0
vowels = ["a", "e", "i", "o", "u"]
for i in sentence:
    if i in vowels:
        count += 1
print(count)
