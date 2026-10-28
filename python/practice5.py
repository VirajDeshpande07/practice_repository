# append this line "This is appended text" to the end of the file without overwriting the text.
file = open("file.txt","a")
file.write("This is appended text!")
file.close()
