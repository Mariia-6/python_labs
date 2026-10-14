def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("Список не может быть пустым")

    current_min = nums[0]
    current_max = nums[0]

    for num in nums[1:]:
        if num < current_min:
            current_min = num
        if num > current_max:
            current_max = num

    return (current_min, current_max)