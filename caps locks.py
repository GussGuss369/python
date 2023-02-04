message = input()
wordlist = list(message)
wordlist2 = []

for letter in wordlist:
    current = ord(letter)
    wordlist2.append(current)


wordlist3 = []
for j in wordlist2:
    if j < 91 and j > 64:
        current = j + 32
        l = chr(current)
        wordlist3.append(l)
    elif j < 123 and j > 96:
        current = j - 32
        u = chr(current)
        wordlist3.append(u)
    else:
        s = chr(j)
        wordlist3.append(s)
done = "".join(wordlist3)
print(done)