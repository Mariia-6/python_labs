input_str = input()
def decrypt_string(s):
    start_idx = -1
    for i, char in enumerate(s):
        if char.isupper():
            start_idx = i
            break


    if start_idx == -1:
        return ''

    step = 0
    for i, char in enumerate(s):
        if char.isdigit():
            second_char_idx = i + 1
            step = second_char_idx - start_idx
            break

    if step <= 0:
        return s[start_idx]

    result = []
    current_idx = start_idx

    while current_idx < len(s):
        char = s[current_idx]
        result.append(char)

        if char == '.':
            break

        current_idx += step

    return ''.join(result)

print(decrypt_string(input_str))