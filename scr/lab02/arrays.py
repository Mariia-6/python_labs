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


def flatten(mat: list[list | tuple]) -> list:
    result = []

    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError(f"Элемент {row} не является списком или кортежем")

        for item in row:
            result.append(item)

    return result

print("min_max")
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
try:
    print(min_max([]))
except ValueError:
    print("ValueError")
print(min_max([1.5, 2, 2.0, -3.1]))

print("unique_sorted")
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

print("flatten")
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
try:
    print(flatten([[1, 2], "ab"]))
except TypeError:
    print("TypeError")