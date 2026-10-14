def _check_rectangular(mat: List[List[Union[float, int]]]) -> None:
    if not mat:
        return
    first_len = len(mat[0])
    for row in mat:
        if len(row) != first_len:
            raise ValueError("Матрица должна быть прямоугольной")

def row_sums(mat: List[List[Union[float, int]]]) -> List[float]:
    _check_rectangular(mat)
    return [sum(row) for row in mat]