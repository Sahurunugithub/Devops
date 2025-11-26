# Take a score as input and print the grade based on the following:

grade = int(input("Enter the grade: "))
print(grade)

# Type 1

if grade >= 90 or grade == 100:
    print("A")
elif grade >= 80 or grade == 89:
    print("B")
elif grade >= 70 or grade == 79:
    print("C")
elif grade >= 60 or grade == 69:
    print("D")
else:
    print("F")





# Type 2:

if 90<=grade<=100:
    print("A")
elif 80<=grade<=89:
    print("B")
elif 70<=grade<=79:
    print("C")
elif 60<=grade<=69:
    
    print("D")
else:
    print("F")





