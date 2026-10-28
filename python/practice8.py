#word frequency counter. Count how many times each word appears in a file and return in a dictionary
file = open("file.txt","r")
data = file.read()
words = data.split()
count={}
for word in words:
    if word in count:
        count[word] = count[word]+1
    else:
        count[word]=1
    print(count)
file.close()
