number = input
low = 1
high = number
guess = (low + high)/2
nsquared = guess**2
while nsquared != number:
    if nsquared > number:
        high = guess
    elif nsquared < number:
        low = guess
    guess = (low + high)/2
    nsquared = guess**2

if nsquared == number:
    print("found")