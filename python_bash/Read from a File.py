'''
4. Read from a File
We used open in read mode and file.read to read and print to display.
'''

def readfile():
    filename = "myfile"

    with open(filename, "r") as file:
        content = file.read()
        print(content)

readfile()


