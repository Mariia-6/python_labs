import re
from collections import Counter

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')

    text = re.sub(r'\s', ' ', text)

    text = re.sub(r' +', ' ', text)
    
    return text.strip()


def tokenize(text: str) -> list[str]:
    pattern = r'\w+(?:-\w+)*'
    return re.findall(pattern, text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    return dict(Counter(tokens))


def top_n(freq: dict[str, int], n: int) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
    
    return sorted_items[:n]

if __name__ == '__main__':
    print("normalize")
    print(f'• "ПрИвЕт\\nмИр\\t" → {normalize("ПрИвЕт\\nмИр\\t")!r}  (casefold + схлопнуть пробелы)')
    print(f'• "Ёжик, Ёлка" (yo2e=True) → {normalize("Ёжик, Ёлка", yo2e=True)!r}')
    print(f'• "Hello\\r\\nWorld" → {normalize("Hello\\r\\nWorld")!r}')
    print(f'• "  двойные   пробелы  " → {normalize("  двойные   пробелы  ")!r}')

    print("\ntokenize (предполагаем, что текст уже normalize)")
    print(f'• "привет мир" → {tokenize("привет мир")!r}')
    print(f'• "hello,world!!!" → {tokenize("hello,world!!!")!r}')
    print(f'• "по-настоящему круто" → {tokenize("по-настоящему круто")!r}')
    print(f'• "2025 год" → {tokenize("2025 год")!r}')
    print(f'• "emojis 😊 не слово" → {tokenize("emojis 😊 не слово")!r} (эмодзи выпадают)')

    print("\ncount_freq + top_n")
    tokens1 = ["a", "b", "a", "c", "b", "a"]
    print(f'• Токены {tokens1!r} → частоты {count_freq(tokens1)!r} ;')
    print(f'  top_n(..., n=2) → {top_n(count_freq(tokens1), 2)!r}')
    
    tokens2 = ["bb", "aa", "bb", "aa", "cc"]
    print(f'• При равенстве частот: токены {tokens2!r} → частоты {count_freq(tokens2)!r} ;')
    print(f'  top_n(..., n=2) → {top_n(count_freq(tokens2), 2)!r} (алфавитная сортировка при равенстве)')