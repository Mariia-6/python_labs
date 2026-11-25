import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

def main() -> None:
    parser = argparse.ArgumentParser(description="CLI-конвертеры данных(JSON, CSV, XLSX)")
    subparsers = parser.add_subparsers(dest= "cmd", required= True, help= "Доступные команды конвертации")

    #json2csv
    p1 = subparsers.add_parser("json2csv", help = "Конвертировать JSON в CSV")
    p1.add_argument("--in", dest= "input", required= True, help= "Путь к входному JSON-файлу")
    p1.add_argument("--out", dest= "output", required= True, help="Путь к выходному CSV-файлу")

    #csv2json
    p2 = subparsers.add_parser("csv2json", help = "Конвертировть CSV в JSON")
    p2.add_argument("--in", dest= "input", required= True, help= "Путь к входному CSV-файлу")
    p2.add_argument("--out", dest= "output", required= True, help= "Путь к выходному JSON-файлу")

    #csv2xlsx
    p3 = subparsers.add_parser("csv2xlsx", help = "Конвертировать CSV в XLSX")
    p3.add_argument("--in", dest= "input", required= True, help= "Путь к входному CSV-файлу")
    p3.add_argument("--out", dest= "output", required= True, help= "Путь к выходному XLSX-файлу")

    args = parser.parse_args()

    if args.cmd == "json2csv": json_to_csv(args.input, args.output)
    elif args.cmd == "csv2json": csv_to_json(args.input, args.output)
    elif args.cmd == "csv2xlsx": csv_to_xlsx(args.input, args.output)

if __name__ == "__main__":
    main()