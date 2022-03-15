done = False
repeat = False
letters = []
word = []
print("Welcome to Guess The Word game")
secret_word = input("Player 1 please enter the secret word: ").lower()
length = len(secret_word)
template = ["."]* length
print(f"the length is {length}")
def repeated(guess, letters):
    if guess in letters:
        print("you have already guessed this letter")
        repeat == True
    else:
        repeat == False
    return repeat
while len(secret_word) > 12 or len(secret_word) < 6:
    secret_word = input("secret word should be between 6 and 12 letters, enter another word: ")
while done == False:
    guess = input("Player 2 enter a letter: ").lower()
    repeat = repeated(guess, letters)
    letters.append(guess)
    if repeat == False:
        for i in secret_word:
            if guess == i:  
                counter = secret_word.count(guess)
                letters.append(guess)
        positions = [i for i, x in enumerate(secret_word) if x == guess]
        for i in positions:
            template[i] = guess
        print(template)
        print(f"letter: {guess} count: {counter}")
        question = input("Do you want to guess the word, enter Y or N: ")
        question = question.upper()
        if question == "Y":
                done = True
guess = input("Player 2 enter the WORD: ").lower()
if guess == secret_word:
    print("Player 2 wins!")
else:
    print("Player 1 wins!")