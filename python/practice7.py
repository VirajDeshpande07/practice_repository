# line numbering print line with its number
file = open("sample.txt","r")
lines = file.readlines()

i = 1
for line in lines:
    print(i, ":",line.strip())
    i = i+1
file.close()
