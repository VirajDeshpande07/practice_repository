#print names in ascending order
with open("names.txt","r") as file:
    names = file.read().splitlines()
names.sort(key=str)
print("Names in alphabetical order: ")
for name in names:
    print(name)
