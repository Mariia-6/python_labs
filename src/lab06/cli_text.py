import argparse
from pathlib import Path
from src.lib.text import normalize, tokenize, count_freq, top_n

def cmd_cat(path: str, number_lines: bool) -> None:
    file_path = Path(path)
    if not file_path.exists(): 
        raise FileNotFoundError(f"Файл {path} не найден")


    with file_path.open("r", encoding= "utf-8") as f:
        for idx, line in enumerate(f, start=1):
            text = line.rstrip("\r\n")
            if number_lines: print(f"{idx}: {text}")
            else: print(text)


def cmd_stats(path: str, top: int) -> None:
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Файл {path} не найден")

    text = file_path.read_text(encoding= "utf-8")
    tokens = tokenize(normalize(text))
    freqs = count_freq(tokens)
    top_words = top_n(freqs, top)

    for word, count in top_words:
        print(f"{word}:{count}")

def main() -> None:
    parser = argparse.ArgumentParser(description= "CLI-утилиты для работы с текстом")
    subparsers = parser.add_subparsers(dest= "command", required= True, help= "Доступные команды")

    cat_parser = subparsers.add_parser("cat", help= "Вывести содержимое файла построчно")
    cat_parser.add_argument("--input", required= True, help= "Путь к входному файлу")
    cat_parser.add_argument("-n", action= "store_true", help= "Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help= "Вывести топ частотных слов в тексте")
    stats_parser.add_argument("--input", required= True, help= "Путь к входному файлу")
    stats_parser.add_argument("--top", type= int, default= 5, help= "Количество топ-слов (по умолчанию 5)")

    args = parser.parse_args()

    if args.command == "cat": cmd_cat(args.input, args.n)
    elif args.command == "stats":
        if args.top <= 0:
            parser.error("Параметр --top должен быть целым положительным числом")
        cmd_stats(args.input,args.top)

if __name__ == "__main__":
    main()
