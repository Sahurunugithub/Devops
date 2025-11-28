'''Create a dictionary where the keys are student names and the values are their grades. Allow the user to:
1.Add a new student and grade.
Update an existing student’s grade.
Print all student grades.
'''

student = {}


# Add New students
def add_student():
    try:
        while True:
            name = input("Enter the name of the student: ")
            grade = int(input("Enter the grade of the student: "))
            student[name] = grade

            choice = input("Do you want to add another student? (y/n): ")
            if choice != "y":
                break
        return student
    
    except:
        print("Invalid input")


#Update Students Grade
def update_student_grade():
    name = input("Enter the name of the student you want to update: ")
    if name in student:
        grade = int(input("Enter the new grade: "))
        student[name] = grade
    else:
        print("Student not found")
    return student


while True:
    choice = int(input("Enter your choice"))
    if choice == 1:
        add_student()
    elif choice == 2:
        update_student_grade()
    elif choice == 3:
        break
    else:
        print("Invalid choice")

# Print All Students
    print("All Students and their grades: ", student)











# for i in range(100):
#     if i % 2== 0:
#         print(i, "is even")




# x = 10

# x += 2   # 12
# x -= 3   # 9
# x *= 2   # 18
# x /= 2   # 9.0
# print(x)
# x %= 4   # 1.0


# x **= 3  # 1.0 ** 3 = 1.0
# x //= 2  # Floor division -> 0.0

# print(x)