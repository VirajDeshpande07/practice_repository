# seek practice jump to 10 th character using seek() and print next 5 characters
file = open("file.txt","r")
file.seek(9)
data = file.read(5)
print(data)
file.close()