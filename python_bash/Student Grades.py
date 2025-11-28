'''Create a dictionary where the keys are student names and the values are their grades. Allow the user to:
Add a new student and grade.
Update an existing student’s grade.
Print all student grades.
'''


students = {}

def add_students():
    name= input("Enter the name of the student: ")
    grade= int(input("Enter the grade of the student: "))
    students[name] = grade

    print(students)
    return students

add_students()








for i in range(100):
    if i % 2== 0:
        print(i, "is even")




x = 10

x += 2   # 12
x -= 3   # 9
x *= 2   # 18
x /= 2   # 9.0
print(x)
x %= 4   # 1.0


x **= 3  # 1.0 ** 3 = 1.0
x //= 2  # Floor division -> 0.0

print(x)