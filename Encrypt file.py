import csv
import base64


def stretchKey(contents,key):
    if len(contents)>len(key):
        f = len(contents)//len(key)
        g = len(contents) - (f*len(key))
        finalKey = (key*f)+key[:g]
        return contents,finalKey
    
    elif len(contents)<len(key):
        finalKey = key[0:len(contents)]
        return contents,finalKey
    
    else:
        return contents,key

    
        
def encryptContents(contents,key):
    finalText = []
    for i,j in zip(contents,key):
        i = ord(i)
        i = i + ord(j)
        finalText.append(chr(i))
    #encryptedContents = ("".join(finalText))
        #finalText.append(i)
        encryptedContents = finalText
    return encryptedContents




def decryptContents(encryptedContents, key):
    finalText = []
    for i,j in zip(encryptedContents,key):
        i = ord(i)
        i = i - ord(j)
        finalText.append(chr(i))
    decryptedContents = ("".join(finalText))
    return decryptedContents

def readFile(fileName):
    try:
        with open(fileName, "r") as textFile:
            fileContents = textFile.read()
            print("Successfully read text file")
    except IOError:
        print("Could not read text file")
    return fileContents

def writeFile(fileName,contents):
    try:
        file = open(fileName,"w")
        file.write(contents)
        file.close()
        print("Successfully written to file")
    except IOError:
        print("Could not write to file")



######################################################        
"""
def writeCSV(fileName, data):
    with open(fileName, 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(data)
"""
######################################################


def readFileBinary(fileName):
    try:
        with open(fileName, "rb") as textFile:
            fileContents = textFile.read()
            print("Successfully read text file")
    except IOError:
        print("Could not read text file")
    return fileContents

def writeFileBinary(fileName, contents):
    try:
        file = open(fileName,"wb")
        file.write(contents)
        file.close()
        print("Successfully written to file")
    except IOError:
        print("Could not write to file")
    
    


def menu(option):
    global stopProgram
    if option==1:
        base64img = readFile(input("Please enter the base64 image path: "))
        key = input("Please enter the password you would like to secure the file with: ")
        contents,password = stretchKey(base64img,key)
        encryptedText = encryptContents(contents,password)
        writeFileBinary(input("What would you like to name the encrypted file?(as text file) "), bytes(("".join(encryptedText)), "utf-8"))

    elif option == 2:
        encryptedText = readFileBinary(input("Please enter the encrypted image path: "))
        encryptedText = encryptedText.decode("utf-8")
        key = input("Please enter the password: ")
        contents,password = stretchKey(encryptedText,key)
        decryptedContents = decryptContents(contents, password)
        writeFileBinary(input("What would you like to name the decrypted file?(as image) "),base64.b64decode(decryptedContents))
        
    elif option == 3:
        stopProgram = True
    
    else:
        menu(int(input("""
Enter 1 to encrypt
      2 to decrypt
      3 to quit
      > """)))


        
stopProgram = 0
while stopProgram == False:
    menu(int(input("""
Enter 1 to encrypt
      2 to decrypt
      3 to quit
      > """)))

