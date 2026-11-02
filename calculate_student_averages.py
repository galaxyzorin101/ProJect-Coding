def calculate_student_averages():

    name1 = input("Please enter your student 1 id number: ")
    name2 = input("Please enter your student 1 name: ")
    name3 = input("Enter your verification pass 1 number: ")
    name4 = input("Please enter your student id 2 number: ")
    name5 = input("Please enter your student 2 name: ")
    name6 = input("Enter your verification pass 2 number: ")
    name7 = input("Please enter your student id 3 number: ")
    name8 = input("Please enter your student 3 name: ")
    name9 = input("Enter your verification pass 3 number: ")


    grade1 = float(input("Student 1, enter your average grade: "))
    grade2 = float(input("Student 2, enter your average grade: "))
    grade3 = float(input("Student 3, enter your average grade: "))

    
    avgGrade = (grade1 + grade2 + grade3) / 3

  
    print(f"The average for all is {avgGrade}")


calculate_student_averages()
