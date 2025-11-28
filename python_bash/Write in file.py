''' 
3.Write to a File
Write a program to create a text file and write some content to it.

Using file functions like write and open.
'''



def file():
    filename = input("Enter the name of the file: ")
    
    with open(filename, "w") as file:
        content = input("Enter the content to write to the file: ")
        file.write(content)
        print(f"{filename} created and content written successfully.")

file()

