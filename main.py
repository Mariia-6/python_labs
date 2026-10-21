import argparse
from pathlib import Path
from collections import Counter
from typing import Iterable

from src.lab04.io_txt_csv import read_text, write_csv

try:
    from src.lib.text import normalize, tokenize, top_n
except ImportError:
    def normalize(s: str) -> str:
        return s.casefold().replace('ё', 'е').replace('\t', ' ').replace('\r', ' ').replace('\n', ' ').strip()
    def tokenize(s: str) -> list[str]:
        import re
        return re.findall(r'\w+(?:-\w+)*', s)
    def top_n(freq: dict, n: int) -> list[tuple[str, int]]:
        return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))[:n]


def print_pretty_table(headers: list[str], rows: list[tuple]) -> None:
    str_headers = [str(h) for h in headers]
    str_rows = [[str(cell) for cell in row] for row in rows]
    
    col_widths = [len(h) for h in str_headers]
    for row in str_rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(cell))
            
    separator = '-+-'.join('-' * w for w in col_widths)
    
    header_line = ' | '.join(f'{h:<{w}}' for h, w in zip(str_headers, col_widths))
    print(header_line)
    print(separator)
    
    for row in str_rows:
        print(' | '.join(f'{c:<{w}}' for c, w in zip(row, col_widths)))


def main():
    parser = argparse.ArgumentParser(description='Анализ частотности слов в текстовых файлах.')
    parser.add_argument(
        '--in', 
        dest='input_files', 
        nargs='+', 
        required=True, 
        help='Пути к входным текстовым файлам (можно несколько через пробел)'
    )
    args = parser.parse_args()

    input_paths = [Path(p) for p in args.input_files]
    
    per_file_rows = []
    total_freq = Counter()

    print('Обработка файлов...')
    
    for path in input_paths:
        try:
            text = read_text(path)
        except FileNotFoundError:
            print(f'Ошибка: Файл {path} не найден. Пропускаем.')
            continue
            
        tokens = tokenize(normalize(text))
        
        file_freq = Counter(tokens)
        
        total_freq.update(file_freq)
        
        sorted_file_items = sorted(file_freq.items(), key=lambda kv: (-kv[1], kv[0]))
        for word, count in sorted_file_items:
            per_file_rows.append((path.name, word, count))


    # Формирование отчетов

    per_file_rows.sort(key=lambda x: (x[0], -x[2], x[1]))
    
    write_csv(
        rows=per_file_rows,
        path='data/report_per_file.csv',
        header=('file', 'word', 'count')
    )
    
    sorted_total_items = sorted(total_freq.items(), key=lambda kv: (-kv[1], kv[0]))
    
    write_csv(
        rows=sorted_total_items,
        path='data/report_total.csv',
        header=('word', 'count')
    )

    print('\n=== Сводный отчет (Топ слов) ===')
    
    top_items = sorted_total_items[:10]
    
    table_headers = ['Слово', 'Частота']
    table_rows = [(word, count) for word, count in top_items]
    
    print_pretty_table(table_headers, table_rows)
    print(f'\nВсего уникальных слов: {len(total_freq)}')
    print('Отчеты сохранены в data/report_per_file.csv и data/report_total.csv')


if __name__ == '__main__':
    main()