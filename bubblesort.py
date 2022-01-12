mylist = [5, 3, 2, 1, 0,]
n = len(mylist)

for i in range(0,n):
    for j in range(0,n-1):
        if mylist[j] > mylist[j+1]:
            mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
print(mylist)

#OR UNIVERSAL CODE AND MORE EFFICIENT

mylist = [5, 3, 2, 1, 0,]
n = len(mylist)

for i in range(0,n):
    for j in range(0,n-1-i):
        if mylist[j] > mylist[j+1]:
            temp = mylist[j]
            mylist[j] = mylist[j+1]
            mylist[j+1] = temp
print(mylist)