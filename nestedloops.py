print("these are the numbers that can be cubed and get the same number: ")

for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            sum = i**3 + j**3 + k**3
            if sum == int(str(i) + str(j) + str(k)):
                print(f"the numbers are: {i}**3 + {j}**3 + {k}**3 = {sum}")