import csv
from pathlib import Path
from openpyxl import Workbook

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    src = Path(csv_path)
    if not src.exists():
        raise FileNotFoundError(csv_path)
    if src.suffix.lower() != '.csv':
        raise ValueError('Ожидается файл .csv')

    with src.open('r', newline = '', encoding = 'utf-8') as f:
        rows = list(csv.reader(f))

    if not rows or not any(rows):
        raise ValueError('CSV пустой или без заголовка')

    wb = Workbook()
    ws = wb.active
    ws.title = 'Sheet1'

    for row in rows:
        ws.append(row)

    for col in ws.columns:
        max_len = max((len(str(cell.value or "")) for cell in col), default = 0)
        ws.column_dimensions[col[0].column_letter].width = max(max_len +2, 8)

    dst = Path(xlsx_path)
    dst.parent.mkdir(parents= True, exist_ok= True)
    wb.save(dst)