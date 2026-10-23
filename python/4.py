#Save the filtered names (longer than 5 characters) into a new file.
with open("names.txt","r") as file:
    names = file.read().splitlines()

filtered_names = []
for name in names:
    if len(name) > 5:
        filtered_names.append(name)

with open("filtered_names.txt","w")as file:
    for name in filtered_names:
        file.write(name + "\n")

print("Successful!")