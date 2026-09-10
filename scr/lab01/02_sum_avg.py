a = float(input('a:').strip().replace(',', '.'))
b = float(input('b:').strip().replace(',', '.'))

sum = a + b
avg = sum / 2
print(f"sum={sum:.2f}; avg={avg:.2f}")