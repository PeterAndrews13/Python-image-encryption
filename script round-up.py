import base64
import zlib


def readImage(fileName):#reads file in binary mode
    try:
        with open(fileName, "rb") as imageFile:
            str1 = base64.b64encode(imageFile.read())
            print("Successfully read",fileName)
    except IOError:
        print("Could not read Image file")
        
    imageString = str1
    return imageString


def readFile(fileName):
    try:
        with open(fileName, "rb") as textFile:
            fileContents = textFile.read()
            print("Successfully read text file")
    except IOError:
        print("Could not read text file")
    return fileContents

def compress(string):
    compressedContents = zlib.compress(string)
    return compressedContents

def decompress(string):
    decompressedContents = zlib.decompress(string)
    return decompressedContents

def writeFile(fileName,contents):
    try:
        file = open(fileName,"wb")
        file.write(contents)
        file.close()
        print("Successfully written to file")
    except IOError:
        print("Could not write to file")
    
def menu():
    print("Please select an option")
    print("""
1) Convert image to base64 string
2) Compress base64 string from file and write to new file
3) Decompress base64 string from file and write to new file
4) Quit
""")
    userInput = input("> ")
    return userInput

runProgram = True
while runProgram:
    choice = menu()
    if choice == "1":
        imageString = readImage(input("Enter image path: "))
        writeFile(input("Enter text file name: "),imageString)
    elif choice == "2":
        fileContents = readFile(input("Enter text file path: "))
        compressedContents = compress(fileContents)
        writeFile(input("Enter text file name: "),compressedContents)
    elif choice == "3":
        fileContents = readFile(input("Enter text file path: "))
        decompressedContents = decompress(fileContents)
        writeFile(input("Enter text file name: "),decompressedContents)
    elif choice == "4":
        runProgram = False
    else:
        print("Invalid selection. Please try again")
