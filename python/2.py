#Print names longer than 5 characters.
with open("names.txt","r") as file:
    names = file.read().splitlines()
for name in names:
    if len(name) > 5:
        print(name)