slow = 0
meduim = 0
fast = 0

def inputData(slow,fast,meduim):
    user = int(input("enter data: "))
    timeTaken = user
    if timeTaken == 0:
        print(slow,fast,meduim)
    elif timeTaken < 30:
        print("under 30")
        fast = fast + 1
        inputData(slow,fast,meduim)
    elif timeTaken < 60:
        print("under 60")
        meduim = meduim + 1
        inputData(slow,fast,meduim)

inputData(slow,meduim,fast)