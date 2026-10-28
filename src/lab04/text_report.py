import argparse, sys
from pathlib import Path
from collections import Counter

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from src.lib.text import normalize, tokenize, top_n
from src.lab04.io_txt_csv import read_text, write_csv

def get_freq(text: str) -> dict[str, int]:
    return dict(Counter(tokenize(normalize(text)))) if text.strip() else {}

def sort_freq(freq: dict) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))

def print_table(headers: list[str], rows: list[tuple]) -> None:
    s_rows = [[str(x) for x in r] for r in rows]
    w = [max([len(h)] + [len(r[i]) for r in s_rows]) for i, h in enumerate(headers)]
    print(" | ".join(h.ljust(w[i]) for i, h in enumerate(headers)))
    print("-+-".join("-" * x for x in w))
    for r in s_rows: print(" | ".join(x.ljust(w[i]) for i, x in enumerate(r)))

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--in", dest="files", nargs="+", required=True)
    p.add_argument("--per-file", dest="pf_csv")
    p.add_argument("--total", dest="tot_csv")
    p.add_argument("--encoding", default="utf-8")
    a = p.parse_args()

    if not a.pf_csv and not a.tot_csv:
        sys.exit("Ошибка: Укажите хотя бы один флаг --per-file или --total.")

    g_freq, pf_data = Counter(), []
    for f_str in a.files:
        f_path = Path(f_str)
        try: text = read_text(f_path, a.encoding)
        except Exception as e: sys.exit(f"Ошибка чтения файла '{f_path}': {e}")

        f_freq = get_freq(text)
        g_freq.update(f_freq)
        pf_data.extend((f_path.name, w, c) for w, c in f_freq.items())

    if a.pf_csv:
        pf_data.sort(key=lambda x: (x[0], -x[2], x[1]))
        write_csv(pf_data, a.pf_csv, ("file", "word", "count"))
        print("--- Отчёт по каждому файлу ---"); print_table(["file", "word", "count"], pf_data); print()

    if a.tot_csv:
        tot_data = sort_freq(g_freq)
        write_csv(tot_data, a.tot_csv, ("word", "count"))
        print("--- Сводный отчёт ---"); print_table(["word", "count"], tot_data); print()

    print(f"=== Краткое резюме ===\nВсего слов: {sum(g_freq.values())}\nУникальных слов: {len(g_freq)}\nТоп-5:")
    for w, c in (top_n(dict(g_freq), 5) or []): print(f"  {w}: {c}")

if __name__ == "__main__":
    main()