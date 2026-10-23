#String analysis: length, first character, last character and palindrome
with open("names.txt","r") as file:
    names = file.read().splitlines()
for name in names:
    if name:
        print("name:",name)
        print("length:",len(name))
        print("first character: ",name[0])
        print("last character: ",name[-1])
    if name.lower() == name[::-1].lower():
        print("Name is palindrome")
    else:
        print("Name is not a palindrome")
print()