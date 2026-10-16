def highestOccurringElement(nums):
    count = {}

    for num in nums:
        count[num] = count.get(num, 0) + 1

    max_count = max(count.values())

    result = []

    for num in count:
        if count[num] == max_count:
            result.append(num)

    return min(result)