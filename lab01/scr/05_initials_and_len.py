full_name = input('ФИО: ')

cleaned_name = ' '.join(full_name.split())
words = cleaned_name.split()

initials = ''
for word in words:
    initials += word[0].upper()
initials += '.'

length = len(cleaned_name)

print(f'Инициалы: {initials}')
print(f'Длина (символов): {length}')