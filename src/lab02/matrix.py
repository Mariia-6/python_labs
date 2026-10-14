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

if __name__ == "__main__":
    print("transpose")
    print(f"{[[1, 2, 3]]} -> {transpose([[1, 2, 3]])}")
    print(f"{[[1], [2], [3]]} -> {transpose([[1], [2], [3]])}")
    print(f"{[[1, 2], [3, 4]]} -> {transpose([[1, 2], [3, 4]])}")
    print(f"{[]} -> {transpose([])}")
    try:
        print(f"{[[1, 2], [3]]} -> {transpose([[1, 2], [3]])}")
    except ValueError:
        print(f"{[[1, 2], [3]]} -> ValueError (рваная матрица)")

    print("row_sums")
    print(f"{[[1, 2, 3], [4, 5, 6]]} -> {row_sums([[1, 2, 3], [4, 5, 6]])}")
    print(f"{[[-1, 1], [10, -10]]} -> {row_sums([[-1, 1], [10, -10]])}")
    print(f"{[[0, 0], [0, 0]]} -> {row_sums([[0, 0], [0, 0]])}")
    try:
        print(f"{[[1, 2], [3]]} -> {row_sums([[1, 2], [3]])}")
    except ValueError:
        print(f"{[[1, 2], [3]]} -> ValueError (рваная матрица)")

    print("col_sums")
    print(f"{[[1, 2, 3], [4, 5, 6]]} -> {col_sums([[1, 2, 3], [4, 5, 6]])}")
    print(f"{[[-1, 1], [10, -10]]} -> {col_sums([[-1, 1], [10, -10]])}")
    print(f"{[[0, 0], [0, 0]]} -> {col_sums([[0, 0], [0, 0]])}")
    try:
        print(f"{[[1, 2], [3]]} -> {col_sums([[1, 2], [3]])}")
    except ValueError:
        print(f"{[[1, 2], [3]]} -> ValueError (рваная матрица)")