def clear_name(file_name: str) -> list:
    """Функция для очистки имен от лишних символов"""
    cleaned_names = []
    with open(file_name, encoding='utf-8') as names_file:
        for line in names_file:
            cleaned = ''.join(c for c in line if c.isalpha())
            if cleaned:
                cleaned_names.append(cleaned)
    return cleaned_names

if __name__ == '__main__':
    names = clear_name('data/names.txt')
    for name in names:
        print(name)
