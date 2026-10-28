#count how many names start with vowel
with open("names.txt","r") as file:
    names = file.read().splitlines()
count = 0
for name in names:
    if name[0].lower() in "aeiou":
        count +=1
print("names starting with vowels: ",count)