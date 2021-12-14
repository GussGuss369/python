def InitialiseStack(stack, pointer):
    stack = []
    pointer = 0
    return stack, pointer

def AddToStack(stack, pointer, item):
    stack.append(item)
    pointer += 1
    return stack, pointer

def RemoveFromStack(stack, pointer):
    del stack[-1]
    pointer -= 1
    return stack, pointer

stack = []
pointer = 0
stack, pointer = InitialiseStack(stack, pointer)
print(f"pointer is now {pointer}")
print(f"stack is now {stack}")
item = input("enter to add to stack")
stack, pointer = AddToStack(stack, pointer, item)
print(f"pointer is now {pointer}")
print(f"stack is now {stack}")
answer = input("do you want to remove from stack?")
if answer == "yes":
    stack, pointer = RemoveFromStack(stack, pointer)
    print(f"pointer is now {pointer}")
    print(f"stack is now {stack}")
else:
    print("okay, bye")