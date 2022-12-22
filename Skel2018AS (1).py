# Skeleton Program for the AQA AS Summer 2018 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA AS Programmer Team
# developed in a Python 3 environment


# Version Number : 1.6

SPACE = ' '
EOL = '#'
EMPTYSTRING = ''

def ReportError(s):
  print('{0:<5}'.format('*'),s,'{0:>5}'.format('*')) 
        
def StripLeadingSpaces(Transmission): 
  TransmissionLength = len(Transmission)
  if TransmissionLength > 0:
    FirstSignal = Transmission[0]
    while FirstSignal == SPACE and TransmissionLength > 0:
      TransmissionLength -= 1
      Transmission = Transmission[1:]
      if TransmissionLength > 0:
        FirstSignal = Transmission[0]
  if TransmissionLength == 0:
    ReportError("No signal received")
  return Transmission

def StripTrailingSpaces(Transmission): 
  LastChar = len(Transmission) - 1
  while Transmission[LastChar] == SPACE:
    LastChar -= 1
    Transmission = Transmission[:-1]
  return Transmission  

def GetTransmission():
  FileName = input("Enter file name: ")
  try:
    FileHandle = open(FileName, 'r')
    Transmission = FileHandle.readline()
    FileHandle.close()
    Transmission = StripLeadingSpaces(Transmission)
    if len(Transmission) > 0:
      Transmission = StripTrailingSpaces(Transmission)
      Transmission = Transmission + EOL
  except:
    ReportError("No transmission found")
    Transmission = EMPTYSTRING
  return Transmission

def GetNextSymbol(i, Transmission):
  if Transmission[i] == EOL:
    print()
    print("End of transmission")
    Symbol = EMPTYSTRING
  else:
    SymbolLength = 0
    Signal = Transmission[i]
    while Signal != SPACE and Signal != EOL:
      i += 1
      Signal = Transmission[i]
      SymbolLength += 1
    if SymbolLength == 1:
      Symbol = '.'
    elif SymbolLength == 3:
      Symbol = '-'
    elif SymbolLength == 0: 
      Symbol = SPACE
    else:
      ReportError("Non-standard symbol received") 
      Symbol = EMPTYSTRING
  return i, Symbol 

def GetNextLetter(i, Transmission):
  SymbolString = EMPTYSTRING
  LetterEnd = False
  while not LetterEnd:
    i, Symbol = GetNextSymbol(i, Transmission)
    if Symbol == SPACE:
      LetterEnd = True
      i += 4
    elif Transmission[i] == EOL:
      LetterEnd = True
    elif Transmission[i + 1] == SPACE and Transmission[i + 2] == SPACE:
      LetterEnd = True
      i += 3
    else:
      i += 1
    SymbolString = SymbolString + Symbol
  return i, SymbolString

def Decode(CodedLetter, Dash, Letter, Dot):
  CodedLetterLength = len(CodedLetter)
  Pointer = 0
  for i in range(CodedLetterLength):
    Symbol = CodedLetter[i]
    if Symbol == SPACE:
      return SPACE
    elif Symbol == '-':
      Pointer = Dash[Pointer]
    else:
      Pointer = Dot[Pointer]
  return Letter[Pointer]

def ReceiveMorseCode(Dash, Letter, Dot): 
  PlainText = EMPTYSTRING
  MorseCodeString = EMPTYSTRING
  Transmission = GetTransmission() 
  LastChar = len(Transmission) - 1
  i = 0
  while i < LastChar:
    i, CodedLetter = GetNextLetter(i, Transmission)
    MorseCodeString = MorseCodeString + SPACE + CodedLetter
    PlainTextLetter = Decode(CodedLetter, Dash, Letter, Dot)
    PlainText = PlainText + PlainTextLetter
  print(MorseCodeString)
  print(PlainText)

def SendMorseCode(MorseCode, v1, v2, v3):
  count = 0 
  PlainText = input("Enter your message (uppercase letters and spaces only): ")
  #caeser cipher here
  newmsg = ""
  for i in PlainText:
    if i == " ":
      i = "@"
    if count == 3:
      count = 0
    count += 1
    if count % 3 == 0:
      if ord(i) + v3 >= 64 and ord(i) + v3 <= 90:
        newchar = ord(i) + v3
        newmsg = newmsg + chr(newchar)
      elif ord(i) + v3 > 90:
        newchar = 64 + ((ord(i) + v3) - 90) 
        newmsg = newmsg + chr(newchar)
      else:
        if ord(i) + v3 < 65:
          newchar = 27 + (ord(i) + v3)
          newmsg = newmsg + chr(newchar)
    elif count % 2 == 0:
      if ord(i) + v2 >= 64 and ord(i) + v2 <= 90:
        newchar = ord(i) + v2
        newmsg = newmsg + chr(newchar)
      elif ord(i) + v2 > 90:
        newchar = 64 + ((ord(i) + v2) - 91)
        newmsg = newmsg + chr(newchar)
      else:
        if ord(i) + v2 < 64:
          newchar = 27 + (ord(i) + v2)
          newmsg = newmsg + chr(newchar)
    else:
      if ord(i) + v1 >= 64 and ord(i) + v1 <= 90:
        newchar = ord(i) + v1
        newmsg = newmsg + chr(newchar)
      elif ord(i) + v1 > 90:
        newchar = 64 + ((ord(i) + v1) - 91) 
        newmsg = newmsg + chr(newchar)
      else:
        if ord(i) + v1 < 64:
          newchar = 26 + (ord(i) + v1)
          newmsg = newmsg + chr(newchar)
  for i in newmsg:
    if i == "@":
      newmsg.replace("@", " ")
  print(newmsg)

  PlainText = newmsg

  PlainTextLength = len(PlainText)
  MorseCodeString = EMPTYSTRING
  for i in range(PlainTextLength):
    PlainTextLetter = PlainText[i]
    if PlainTextLetter == SPACE:
      Index = 0
    elif PlainText[i].isupper() == False or PlainText[i].isspace == False:
      ReportError("Invalid character")
      Index = 0
      MorseCodeString = EMPTYSTRING
      break
    else: 
      Index = ord(PlainTextLetter) - ord('A') + 1
    CodedLetter = MorseCode[Index]
    MorseCodeString = MorseCodeString + CodedLetter + SPACE
  print(MorseCodeString)

def DisplayMenu():
  print()
  print("Main Menu")
  print("=========")
  print("R - Receive Morse code")
  print("S - Send Morse code")
  print("X - Exit program")
  print("A - Print Letters")
  print()

def GetMenuOption():
  MenuOption = EMPTYSTRING
  while len(MenuOption) != 1:
    MenuOption = input("Enter your choice: ")
  return MenuOption
    
def SendReceiveMessages():
  Dash = [20,23,0,0,24,1,0,17,0,21,0,25,0,15,11,0,0,0,0,22,13,0,0,10,0,0,0]
  Dot = [5,18,0,0,2,9,0,26,0,19,0,3,0,7,4,0,0,0,12,8,14,6,0,16,0,0,0]
  Letter = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  MorseCode = [' ','.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
  v1 = int(input("enter the first value key: "))
  v2 = int(input("enter the second value key: "))
  v3 = int(input("enter the third vallue key: "))
  ProgramEnd = False
  while not ProgramEnd:
    DisplayMenu() 
    MenuOption = GetMenuOption()
    if MenuOption == 'R':
      ReceiveMorseCode(Dash, Letter, Dot)
    elif MenuOption == 'S':
      SendMorseCode(MorseCode, v1, v2, v3)
    elif MenuOption == 'X':
      ProgramEnd = True
    elif MenuOption == 'A':
      OutputAlphabetWithCode()

def SendSignals(strt):
  newstr = EMPTYSTRING
  dictd = {
    ".": "=$",
    "-": "===$",
    " ": "$$"
  }

  for x in strt:
    for i in dictd:
      if x == i:
        newstr += dictd[i]
  print(newstr)

def OutputAlphabetWithCode():
  counters = 0
  finstr = ""
  Letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  MorseCode = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
  for i in Letter:
    counters += 1
    if len(MorseCode[counters - 1]) == 1:
      MorseCode[counters - 1] += "   "
    elif len(MorseCode[counters - 1]) == 2:
      MorseCode[counters - 1] += "  "
    elif len(MorseCode[counters - 1]) == 3:
      MorseCode[counters - 1] += " "
    else:
      pass
    if counters % 4 == 0:
      finstr += i + " " + MorseCode[counters - 1] + "\n"
    else:
      finstr += i + " " + MorseCode[counters - 1] + "  "
  print(finstr)

if __name__ == "__main__":
  SendReceiveMessages()