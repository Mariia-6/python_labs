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

print(f'("Иванов Иван Иванович", "BIVT-25", 4.6) → "{format_record(("Иванов Иван Иванович", "BIVT-25", 4.6))}"')
print(f'("Петров Пётр", "IKBO-12", 5.0) → "{format_record(("Петров Пётр", "IKBO-12", 5.0))}"')
print(f'("Петров Пётр Петрович", "IKBO-12", 5.0) → "{format_record(("Петров Пётр Петрович", "IKBO-12", 5.0))}"')
print(f'("  сидорова  анна   сергеевна ", "ABB-01", 3.999) → "{format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999))}"')