#Print names that contain the letter "a".
with open("names.txt","r") as file:
    names = file.read().splitlines()

for name in names:
    if "a" in name.lower():
        print(name)