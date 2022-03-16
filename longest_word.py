def longest_word(str):
    maximum = 0
    longest = ""
    listt = str.split()
    for i in listt:
        if len(i) > maximum:
            maximum = len(i)
            longest = i
    print(f"longest word is {longest} with {maximum} letters")
user = input("enter the sentence: ")
longest_word(user)