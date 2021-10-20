#ceasar cypher code
final = ""
def file():
    f = open("ceaser.txt", "a")
    f.write(final)
    f.close()

def encrypt_p(msg, shift):
    new_msg = ""
    for letter in msg:
        if letter == " " or letter == "," or letter == "." or letter == "(" or letter == ")" or letter.isnumeric():
            new_letter = letter
            new_msg = new_msg + letter
        if letter.isupper():
            new_letter = (shift + ord(letter) - 65) % 26 + 65
            new_msg = new_msg + chr(new_letter)
        elif letter.islower():
            new_letter = (shift + ord(letter) - 97) % 26 + 97
            new_msg = new_msg + chr(new_letter)
    print(new_msg)
    final = new_msg
    return final
    file()

def decrypt_p(msg, shift):
    shift = -shift
    encrypt_p(msg, shift)

def encrypt_n(msg, shift):
    decrypt_p(msg, shift)

def decrypt_n(msg, shift):
    encrypt_p(msg, shift)

question = input("enter e for encrypting, or d for decrypting: ").lower()
shift = int(input("enter the shift: "))
sign = input("enter p for a positive shift, or n for a negative shift: ").lower()
msg = input("enter your message: ")

if question == "e" and sign == "p":
    encrypt_p(msg, shift)
elif question == "e" and sign == "n":
    encrypt_n(msg, shift)
elif question == "d" and sign == "p":
    decrypt_p(msg, shift)
elif question == "d" and sign == "n":
    decrypt_n(msg, shift)