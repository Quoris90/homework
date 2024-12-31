def single_root_words(root_word, *other_words):
    # Приводим корневое слово к нижнему регистру
    root_word_lower = root_word.lower()
    # Создаем пустой список для подходящих слов
    same_words = []

    # Перебираем слова в other_words
    for word in other_words:
        # Приводим текущее слово к нижнему регистру
        word_lower = word.lower()
        # Проверяем, содержит ли root_word слово или наоборот
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)

    # Возвращаем сформированный список
    return same_words


# Пример вызова функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)  
print(result2)
