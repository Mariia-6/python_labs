import sys
import os
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib.text import normalize, tokenize, count_freq, top_n

parser = argparse.ArgumentParser(description="Статистика текста")
parser.add_argument('--table', action='store_true')
args = parser.parse_args()

text = sys.stdin.read()
tokens = tokenize(normalize(text))
freq = count_freq(tokens)
top_5 = top_n(freq, 5)

print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(freq)}")
print("Топ-5:")

if top_5:
    if args.table:
        w = max(len(word) for word, _ in top_5) + 2
        print(f"{'слово':<{w}}| частота")
        print('-' * (w + 9))
        for word, count in top_5:
            print(f"{word:<{w}}| {count}")
    else:
        for word, count in top_5:
            print(f"{word}:{count}")