# python_labs
# Лабораторная работа №2
## Задание A

### Функция 1 (A)

min_max

``` python
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
```
Создаю функцию min_max, которая ожидает список(list), элементы которого дробные(float) или целочисленные, возвращает кортеж(tuple) из двух чисел(оба float | int).

Проверяю список nums на пустоту, если верно - вывожу ValueError.

Принимаю значения текущего минимума(current_min) и текущего максимума(current_max) за первый элемент списка(nums[0]), в качестве стартовой точки для сравнения.

Циклом 'for i in' делаю срез, начиная с индекса 1 (0 учли выше), на каждом шаге переменная-итератор num получает очередной элемент.

Если очередное число меньше текущего минимума — обновляем минимум.

Аналогично для максимума.

Возвращается результат - кортеж из двух значений: минимум и максимум.

#### Тест-кейсы:


### Функция 2 (A)

#### unique_sorted 

``` python
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
```

Объявляю функцию, которая принимает список чисел, возвращает список чисел.

Если список на входе пуст - сразу возвращается пустой список. Если не пуст - идём дальше.

Превращаю список во множество, чтобы не хранить дубликаты(set(nums)). <br>
Превращаю множество обратно в список, так как дальнейшая работа должна проводиться именно с этим форматом(list()).<br>
Результат присваиваю unique_nums.

Прохожу 'for i in():' по длине списка(len(unique_nums)) от 1 индекса(0 считается "уже отсортированной частью").<br>
По сортировке вставками беру i-элемент и вставляю в правильной место в отсортированной части(слева).

Запоминаем текущий элемент в переменной key.<br>
j - индекс элемента слева от key, от него начинаем сдвигать все элементы вправо, чтобы освободить место под key.

Циклом while иду, пока не выхожу за левую границу массива и пока элемент слева больше key.

Сдвигаю элемент с позиции j на j +1(вправо), потом уменьшаем j на 1, переходим к следующему элементу слева.

Когда while остановился - (j +1) - это "дырка", куда нужно положить key. 

Возвращаю отсортированный список уникальных значений.

#### Тест-кейсы:



### Функция 3 (A)

#### flatten

```python
def flatten(mat: list[list | tuple]) -> list:
    result = []

    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError(f"Элемент {row} не является списком или кортежем")

        for item in row:
            result.append(item)

    return result
```

Задаю функцию flatten, где mat - параметр: список, элементы которого - списки или кортежи(т.е. матрицы), возвращается просто список (list).

Создаю пустой список result, чтобы вкладывать в него "расплющенные" элементы.

Прохожу по кадому элементу row внешнего списка mat.<br>
Проверяю (isinstance(row, (list,tuple))) является ли row списком или кортежем(второй аргумент - кортеж типов).<br>
Если не является - выбрасываю TypeError.

Внутренним циклом 'for item in row' иду по элементам строки row.<br>
Добавляю(result.append(item)) элемент в конец списка result.

Возвращаю полученный "плоский" список.

#### Тест-кейсы:



## Задание B

#### Проверка прямоугольности

``` python
def _check_rectangular(mat: List[List[Union[float, int]]]) -> None:
    if not mat:
        return
    first_len = len(mat[0])
    for row in mat:
        if len(row) != first_len:
            raise ValueError("Матрица должна быть прямоугольной")
```
Задаю внутреннюю функцию _check_rectangular с параметром mat: список списков, где элементы - xbck(int или float), она ничего не возвращает(-> None), только проверяет и, при необходимости, бросает исключение.<br>
Если mat - пустой список(такая матрица автоматически становится прямоугольной), проверять нечего - выхожу из функции через return.

Запоминаю длину первой строки матрицы как эталон. Все остальные должны быть той же длины.

Прохожу циклом 'for row in mat' по каждой строке матрицы, на каждой итерации row - это очередной список(строка).

Если длина текущей строки не совпдает с эталоном - матрица "рваная", бросаю исключение ValueError.

### Функция 1 (B)

#### transpose(mat: list[list[float | int]]) -> list[list]

```python
def transpose(mat: List[List[Union[float, int]]]) -> List[List[Union[float, int]]]:
    _check_rectangular(mat)
    if not mat:
        return []
    return [list(row) for row in zip(*mat)]
```
Объявляю функцию transpose: принимает матрицу, возвращает матрицу того же типа.

Вызываю проверку прямоугольности(_check_rectangular(mat)). Если матрица рваная - вылетит ValueError и дальше код не пойдет.

Если матрица пустая - возвращаю пустой список.

Транспонирование:<br>
*mat - распаковывает список строк в отдельные агументы по формату zip(mat[0], mat[1], ..., mat[n-1]).<br>
zip идет по элементам параллельно: берет первые элементы каждой строки, потом вторые и т.д. Получаются столбцы исходной матрицы.<br>
Внешние [...] собирают всё в список списков.

#### Тест-кейсы:


### Функция 2 (B)

#### row_sums(mat: list[list[float | int]]) -> list[float]

```python
def row_sums(mat: List[List[Union[float, int]]]) -> List[float]:
    _check_rectangular(mat)
    return [sum(row) for row in mat]
```

Объявляю функцию row_nums: принимает матрицу, возвращает список чисел(суммы по строкам).

Проверяю прямоугольность(_check_rectangular(mat)).

Списковое включение: для каждой строки row вызываем встроенную sum(row) - собираю результаты в список.<br>
Для [] цикл не выполнится ни разу - вернется [].

#### Тест-кейсы:



### Функция 3 (B)

#### col_sums(mat: list[list[float | int]]) -> list[float]

``` python
def col_sums(mat: List[List[Union[float, int]]]) -> List[float]:
    _check_rectangular(mat)
    if not mat:
        return []
    transposed = transpose(mat)
    return [sum(row) for row in transposed]
```

Объявляю функцию col_nums: принимает матрицу, возвращает список сумм по столбцам.

Проверяю прямоугольность(_check_rectangular(mat)).

Если матрица пустая - столбцов нет, возвращаю [].

Транспонирование матрицы(transpose(mat)): столбцы исходной - строки итоговой. Теперь сумма "по столбцу" сведена к сумме "по строке".

Для каждой строки транспонированной матрицы(=каждого исходного столбца) считаю сумму, собираю в список.

#### Тест-кейсы:



## Задание C

### Пункт 1(C)

#### Определение типа записи студента как кортежа

```python
def format_record(rec: tuple[str, str, float]) -> str:
```

Реализовывается в сигнатуре функции: rec: tuple[str, str, float].<br>
В рантайме этот тип гарантируется проверками ниже:<br>
if not isinsistance(rec, tuple) or len(rec) != 3: - кортеж из 3 элементов.<br>
if not isinsistance(name,str) or not isinsistance(group, str): - первые два поля - строки.<br>
if not isinsistance(gpa, bool) or not isinsistance(gpa, (int, float)): - третье - число.

### Пункт 2(C)

#### Реализация format_record(rec: tuple[str, str, float]) -> str

```python
def format_record(rec: tuple[str, str, float]) -> str:
    if not isinstance(rec, tuple) or len(rec) != 3:
        raise ValueError('Все поля должны быть заполнены')

    name, group, gpa = rec

    if not isinstance(name, str) or not isinstance(group, str):
        raise TypeError('Имя и группа должны быть строками')
    if isinstance(gpa, bool) or not isinstance(gpa, (int, float)):
        raise TypeError('GPA должно быть числом')
    if not (0.0 <= gpa <= 5.0):
        raise ValueError('GPA должен быть в диапазоне от 0.0 до 5.0')

    parts = name.strip().split()
    if len(parts) not in (2, 3):
        raise ValueError('ФИО должно содержать 2 или 3 слова')

    initials = ''.join(p[0].upper() + '.' for p in parts[1:])
    group = group.strip()
    if not group:
        raise ValueError('Группа не может быть пустой')

    return f'{parts[0].capitalize()} {initials}, гр. {group}, GPA {gpa:.2f}'
```

Объявляю функцию format_record: принимает параметр rec - кортеж, состоит из: строка(str), строка(str), дробное число(float). Возвращает строку(-> str).

Проверяю входные данные на соблюдения формата кортежа из 3 элементов. Если формат не соблюден - вывожу ValueError(ошибку значения).

Распаковываю кортеж на отдельные переменные - name(ФИО), group(группа), gpa(средний балл по оценкам).

Проверяю, что name и group - строки, если нет - вывожу TypeError.

Проверяю, что gpa - число(int или float), а не логическое(булевое) значение(bool). Если нет - вывожу TypeError.

Проверяю, что gpa в диапазоне от 0.0 до 5.0. Если нет - вывожу ValueError.

Разбиваю ФИО(name) на отдельные слова, убирая лишние символы. Сохраняю в список parts.

Проверяю, что длина ФИО(len(parts)) - 2 или 3 слова. Если нет - вывожу ValueError.

Формирую строку initials для записи инициалов в нее.<br>
Срезаю список(parts[1:]), беру все, кроме первого элемента, так как первый - фамилия.<br>
Циклом 'for p in parts[1:]' для каждого временного имени p для текущего слова беру первый символ слова(p[0]), использую '.upper()', чтобы сделать букву заглавной. Приклеиваю точку после заглавной буквы.<br>
Методом строки '''.join(...)' склеиваю элементы последовательности в одну строку без разделителя.<br>
Итог сохраняю в переменную initials.

Убираю пробелы в начале и конце названия группы(group.strip()).

Проверяю, что группа не пустая. Если после очистки группа пустая - вывожу ValueError.

Собираю ответ и возвращаю его.<br>
(Беру первый элемент parts[0] - фамилию, вызываю capitalize(), чтобы первая буква была заглавная. Вставляю сформированные ранее инициалы initials, текст ', гр.', название группы group, текст ', GPA', gpa с форматной спецификацией .2f(округление до сотых).)

#### Тест-кейсы:
