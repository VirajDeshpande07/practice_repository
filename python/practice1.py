# Read first line.Write a program to open a text file and print the first line.
file = open("sample.txt","r")
line = file.readline()
print(line)
file.close()