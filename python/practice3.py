# count characters read a file and print total number of characters
file = open("Sample.txt","r")
data = file.read()
print("total number of characters: ",(len(data)))
file.close()