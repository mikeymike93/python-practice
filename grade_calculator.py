name= input("Enter the student's name: ")

grade1= float(input("Enter the first grade: "))
grade2= float(input("Enter the second grade: "))
grade3= float(input("Enter the third grade: "))

average= (grade1 + grade2 + grade3) / 3

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
