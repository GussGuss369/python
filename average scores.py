counter = 0
average = 0
finished = False
scores = []
names = []
grades = []

while finished == False:
    name = input("enter the name of the student or f to finish: ")
    grade = int(input("enter the grade, or x to stop: "))
    if grade == -1 and name == "f":
        finished = True
    else:
        scores.append((name,grade))
        names.append(name)
        grades.append(grade)
    if grade > 10 or (grade < 0 and grade != -1):
        print("invalid input")
    elif grade>= 0 and grade <= 10:
        counter += 1
        average = average + grade

print(f"average is {average/counter} for {counter} grades")
print(scores)
print(f"highest is {max(grades)} by {names[grades.index(max(grades))]} and the lowest is {min(grades)} by {names[grades.index(min(grades))]}")