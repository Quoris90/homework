def calculate_structure_sum(data):
    total_sum = 0

    # Вспомогательная функция для рекурсивной обработки каждого элемента
    def process_element(element):
        nonlocal total_sum

        if isinstance(element, (int, float)):  # Проверка, является ли элемент числом
            total_sum += element
        elif isinstance(element, str):  # Проверка, является ли элемент строкой
            total_sum += len(element)
        elif isinstance(element, (list, tuple, set)):  # Проверка, является ли элемент списком, кортежем или множеством
            for item in element:
                process_element(item)
        elif isinstance(element, dict):  # Проверка, является ли элемент словарём
            for key, value in element.items():
                process_element(key)
                process_element(value)

    # Начало обработки входных данных
    process_element(data)

    return total_sum


# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
