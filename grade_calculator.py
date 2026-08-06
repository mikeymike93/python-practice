name= input("Enter the student's name: ")

grade1= float(input("Enter the first grade: "))
grade2= float(input("Enter the second grade: "))
grade3= float(input("Enter the third grade: "))

average= (grade1 + grade2 + grade3) / 3

print(f"{name}'s average grade is {average:.2f}")