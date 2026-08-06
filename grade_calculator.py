name= input("Enter the student's name: ")

grades = []
for i in range(3):
    grade= float(input(f"Enter grade {i+1}: "))
    grades.append(grade)

average= sum(grades)/len(grades)

if average >=90:
    letter_grade= "A"
elif average >=80:
    letter_grade= "B"
elif average >=70:
    letter_grade= "C"
elif average >=60:
    letter_grade= "D"
else:
    letter_grade= "F"

if average < 60:
    status= "failing"
else:
    status= "passing"

print(f"{name}'s average grade is {average:.2f}, which is a {letter_grade}, and they are {status}.")