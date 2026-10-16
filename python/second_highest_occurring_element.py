
def secondHighestOccurringElement(nums):
    count = {}

    for num in nums:
        count[num] = count.get(num, 0) + 1

    frequencies = sorted(set(count.values()), reverse=True)

    if len(frequencies) < 2:
        return -1

    second_max = frequencies[1]
    result = []

    for num in count:
        if count[num] == second_max:
            result.append(num)

    return min(result)
