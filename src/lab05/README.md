# ЛР5 — JSON и конвертации (JSON↔CSV, CSV→XLSX): Техническое задание

## Описание форматов данных
* **JSON (JavaScript Object Notation)** — текстовый формат обмена данными на основе пар «ключ–значение» и упорядоченных списков. Поддерживает вложенность и типы данных (строки, числа, булевы значения, `null`).
* **CSV (Comma-Separated Values)** — табличный текстовый формат, где строки разделяются переносом строки, а столбцы — запятой `,`. Не хранит типы данных (все значения читаются как строки) и не поддерживает вложенную структуру.
* **XLSX (Office Open XML Workbook)** — бинарный формат электронных таблиц Excel. Поддерживает несколько листов и настройку ширины столбцов.

## Принятые допущения и особенности реализации
* **Кодировка:** все операции чтения и записи выполняются строго в `UTF-8`.
* **Порядок колонок при `JSON → CSV`:** формируется по порядку первого появления ключей в объектах входного списка (`dict.fromkeys`). Отсутствующие у части объектов поля заполняются пустой строкой `""`.
* **Типы данных при `CSV → JSON`:** все значения сохраняются как строки (`str`).
* **Автоширина в `CSV → XLSX`:** активный лист именуется `Sheet1`, ширина каждой колонки рассчитывается по формуле `max(максимальная_длина_текста + 2, 8)`.
* **Валидация:** при отсутствии входного файла выбрасывается `FileNotFoundError`; при неверном расширении, пустом файле или нарушении структуры (например, JSON не является списком словарей) — `ValueError`.

## Задание А — Конвертация JSON ↔ CSV (`src/lab05/json_csv.py`)

```python
import csv
import json
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    src = Path(json_path)
    dst = Path(csv_path)

    if not src.exists():
        raise FileNotFoundError(f"Файл {json_path} не найден")
    if src.suffix.lower() != ".json":
        raise ValueError("Ожидается файл с расширением .json")

    try:
        with src.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError("Некорректный формат JSON") from e

    if not isinstance(data, list) or not data or not all(isinstance(item, dict) for item in data):
        raise ValueError("JSON должен содержать непустой список словарей")

    fieldnames = list(dict.fromkeys(key for row in data for key in row.keys()))
    dst.parent.mkdir(parents=True, exist_ok=True)

    with dst.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, restval="")
        writer.writeheader()
        writer.writerows({k: ("" if v is None else v) for k, v in row.items()} for row in data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    src = Path(csv_path)
    dst = Path(json_path)

    if not src.exists():
        raise FileNotFoundError(f"Файл {csv_path} не найден")
    if src.suffix.lower() != ".csv":
        raise ValueError("Ожидается файл с расширением .csv")

    with src.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError("CSV файл пустой или не содержит заголовков")
        rows = list(reader)

    if not rows:
        raise ValueError("CSV файл не содержит данных")

    dst.parent.mkdir(parents=True, exist_ok=True)
    with dst.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
```

**Команды запуска (`JSON ↔ CSV`):**
```bash
# JSON -> CSV
python -c "from src.lab05.json_csv import json_to_csv; json_to_csv('data/samples/people.json', 'data/out/people_from_json.csv')"
python -c "from src.lab05.json_csv import json_to_csv; json_to_csv('data/samples/books.json', 'data/out/books_from_json.csv')"

# CSV -> JSON
python -c "from src.lab05.json_csv import csv_to_json; csv_to_json('data/samples/people.csv', 'data/out/people_from_csv.json')"
python -c "from src.lab05.json_csv import csv_to_json; csv_to_json('data/samples/courses.csv', 'data/out/courses_from_csv.json')"
```

## Задание В — Конвертация CSV → XLSX (`src/lab05/csv_xlsx.py`)

```python
import csv
from pathlib import Path
from openpyxl import Workbook
from openpyxl.utils import get_column_letter


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    src = Path(csv_path)
    dst = Path(xlsx_path)

    if not src.exists():
        raise FileNotFoundError(f"Файл {csv_path} не найден")
    if src.suffix.lower() != ".csv":
        raise ValueError("Ожидается файл с расширением .csv")

    with src.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))

    if not rows or not any(rows):
        raise ValueError("CSV файл пустой")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in rows:
        ws.append(row)

    for col_idx, col in enumerate(ws.columns, start=1):
        max_len = max((len(str(cell.value)) for cell in col if cell.value is not None), default=0)
        ws.column_dimensions[get_column_letter(col_idx)].width = max(max_len + 2, 8)

    dst.parent.mkdir(parents=True, exist_ok=True)
    wb.save(dst)
```

**Команды запуска (`CSV → XLSX`):**
```bash
python -c "from src.lab05.csv_xlsx import csv_to_xlsx; csv_to_xlsx('data/samples/people.csv', 'data/out/people.xlsx')"
python -c "from src.lab05.csv_xlsx import csv_to_xlsx; csv_to_xlsx('data/samples/cities.csv', 'data/out/cities.xlsx')"
python -c "from src.lab05.csv_xlsx import csv_to_xlsx; csv_to_xlsx('data/samples/movies.csv', 'data/out/movies.xlsx')"
```

### Скриншоты работы
![Конвертация JSON в CSV](images/lab05/01_json_to_csv.png)
![Конвертация CSV в JSON](images/lab05/02_csv_to_json.png)
![Конвертация CSV в XLSX](images/lab05/03_csv_to_xlsx.png)
![Результат в LibreOffice Calc](images/lab05/04_xlsx_preview_people.png)
![Результат в LibreOffice Calc](images/lab05/04_xlsx_preview_movies.png)