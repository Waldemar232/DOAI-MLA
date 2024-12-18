def remove_and_count_a(sentence):
    # Инициализируем счетчик удаленных букв 'а'
    count_a = 0

    # Создаем новое предложение без букв 'а'
    new_sentence = ""

    for char in sentence:
        if char.lower() == 'а':
            count_a += 1
        else:
            new_sentence += char

    return new_sentence, count_a

# Пример использования
sentence = input("Введите предложение: ")
new_sentence, count_a = remove_and_count_a(sentence)
print("Новое предложение:", new_sentence)
print("Количество удаленных букв 'а':", count_a)