def unique_sorted(nums: list[float | int]) -> list[float | int]:
    if not nums:
        return []

    unique_nums = list(set(nums))

    for i in range(1, len(unique_nums)):
        key = unique_nums[i]
        j = i - 1
        while j >= 0 and unique_nums[j] > key:
            unique_nums[j + 1] = unique_nums[j]
            j -= 1
        unique_nums[j + 1] = key

    return unique_nums