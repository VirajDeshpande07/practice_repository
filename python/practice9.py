# comapre 2 files are return whether they are identical or not
file1 = open("file1.txt","r")
data1 = file1.readlines()
file1.close()

file2 = open("file2.txt","r")
data2 = file2.readlines()
file2.close()

if data1==data2:
    print("files are identical!")
else:
    print("files are not identical")