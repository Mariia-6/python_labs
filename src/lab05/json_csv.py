import csv
import json
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    src = Path(json_path)
    if not src.exists():
        raise FileNotFoundError(json_path)
    if src.suffix.lower() != '.json':
        raise ValueError('Ожидается файл .json')

    try:
        data = json.loads(src.read_text(encoding = ('utf-8')))
    except json.JSONDecodeError as e:
        raise ValueError('Пустой или некорректный JSON') from e

    if not data or not isinstance(data, list) or not all(isinstance(x, dict) for x in data):
        raise ValueError('JSON должен быть непустым списком словарей')

    fieldnames = list(dict.fromkeys(k for row in data for k in row))

    dst = Path(csv_path)
    dst.parent.mkdir(parents = True, exist_ok = True)
    with dst.open('w', newline = '', encoding = 'utf-8') as f:

        writer = csv.DictWriter(f, fieldnames=fieldnames, restval = '')
        writer.writeheader()
        writer.writerows({k: ('' if v is None else v) for k,v in row.items()} for row in data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    src = Path(csv_path)
    if not src.exists():
        raise FileNotFoundError(csv_path)
    if src.suffix.lower() != '.csv':
        raise ValueError('Ожидается файл .csv')

    with src.open('r', newline = '', encoding = 'utf-8') as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError('CSV пустой или без заголовка')
        rows = list(reader)

        if not rows:
            raise ValueError('CSV не содержит данных')

        dst = Path(json_path)
        dst.parent.mkdir(parents = True, exist_ok = True)
        dst.write_text(json.dumps(rows, ensure_ascii = False, indent = 2), encoding = 'utf-8')