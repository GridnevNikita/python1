import re



def clear_name(file_name: str) -> list:
    """Функция для очистки имен от лишних символов"""
    cleaned_names = []
    with open('data/' + file_name, encoding='utf-8') as names_file:
        for line in names_file:
            cleaned = ''.join(c for c in line if c.isalpha())
            if cleaned:
                cleaned_names.append(cleaned)
    return cleaned_names


def is_cyrillic(name_item: str) -> bool:
    """Проверка на вхождение кириллицы в строку"""
    return bool(re.search('[а-яА-Я]', name_item))


def filter_russian_name(name_list: list) -> list:
    """Фильтрация имён написанных на русском языке"""
    new_name_list = list()
    for name_item in name_list:
        if is_cyrillic(name_item):
            new_name_list.append(name_item)
    return new_name_list


def save_to_file(file_name: str, data: str) -> None:
    """Сохраняет данные в файл"""
    with open('data/' + file_name, 'w', encoding='utf-8') as names_file:
        names_file.write(data)


if __name__ == '__main__':
    names = clear_name('names.txt')

    filtered_names = (filter_russian_name(names))
    save_to_file('russian_name.txt', '\n'.join(filtered_names))
