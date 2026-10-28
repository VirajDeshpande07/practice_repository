#Read a file containing student names (one per line) and store them in a list.
with open("names.txt","r") as file:
    names = file.read().splitlines()
print(names)