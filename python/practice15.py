# word frequency
with open("names.txt","r") as file:
    names = file.read().splitlines()
frequency = {}
for name in names:
    if name in frequency:
        frequency[name]+=1
    else:
        frequency[name]=1
print(frequency)