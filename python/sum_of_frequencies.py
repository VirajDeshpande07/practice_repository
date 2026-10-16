
def sumOfFrequencies(arr):
    count = {}

    for num in arr:
        count[num] = count.get(num, 0) + 1

    highest = max(count.values())
    lowest = min(count.values())

    return highest + lowest
