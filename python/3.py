#Count how many names start with a vowel
with open("names.txt","r") as file:
    names = file.read().splitlines()

count = 0
for name in names:
    if name and name[0].lower() in "aeiou":
        count+=1
print("Names starting with vowels: ",count)