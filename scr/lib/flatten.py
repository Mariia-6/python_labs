def flatten(mat: list[list | tuple]) -> list:
    result = []

    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError(f"Элемент {row} не является списком или кортежем")

        for item in row:
            result.append(item)

    return result