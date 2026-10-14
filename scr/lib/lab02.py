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



from typing import List, Union

def _check_rectangular(mat: List[List[Union[float, int]]]) -> None:
    if not mat:
        return
    first_len = len(mat[0])
    for row in mat:
        if len(row) != first_len:
            raise ValueError("Матрица должна быть прямоугольной")

def transpose(mat: List[List[Union[float, int]]]) -> List[List[Union[float, int]]]:
    _check_rectangular(mat)
    if not mat:
        return []
    return [list(row) for row in zip(*mat)]

def row_sums(mat: List[List[Union[float, int]]]) -> List[float]:
    _check_rectangular(mat)
    return [sum(row) for row in mat]

def col_sums(mat: List[List[Union[float, int]]]) -> List[float]:
    _check_rectangular(mat)
    if not mat:
        return []
    transposed = transpose(mat)
    return [sum(row) for row in transposed]

