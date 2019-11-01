import os #import the OS library

filePath = '/users/Cassi/Desktop/Assigment10/'
fileName = 'directoryUser.txt'
completePath = filePath+fileName

print("Welcome to Information Directory!")

directoryChosen = input("Please enter a directory:")
fileChosen = input("Please enter a file name:")

name = input("Please enter your first and last name:")
address = input("Please enter your address:")
number = input("Please enter your phone number, including area code:")

if os.path.isfile(fileChosen): #check that file exists
    print("File Exists")
if os.path.isdir(directoryChosen): #check that file path exists
    print("Directory Exists")
if os.path.exists(completePath): #check that complete path exists
    print("Complete Path Exists")

w('name, + number, +address)
print('name,  + number,  + address')

with open(completePath, 'w') as fileHandle: #open file to write
    fileHandle.write("Adding this to file.") #written data to file
with open(completePath, 'r') as fileHandle: #open same file for reading
    data = fileHandle.read() #read data from file
    print(data)
