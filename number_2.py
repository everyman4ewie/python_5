# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.

# 1 вариант
lines = 0  # подсчет строк
words = 0  # подсчет слов
characters = 0  # подсчет букв
with open('filess.txt', 'r', encoding='utf-8') as file:
    for line in open('filess.txt', 'r'):
        lines += 1
        characters += len(line)  # количество символов в строке
        position = 'quit'  # ококнчание слова (флаг), для определения нового слова и пропуск пробела

        for character in line:  # Цикл перебора строки по символам.
            if character != ' ' and position == 'quit':
                words += 1  # Поэтому надо увеличить счетчик слов на 1
                position = 'exit'  # меняем флаг на другое значение элемента внутри слова
            elif character == ' ':  # если символ опять пробел, то устанавливаем начальный флаг.
                position = 'quit'
    # Вывод количеств строк, слов и символов на экран.
    print('Количество строк: ', lines)
    print('Количество слов: ', words)
    print('Количество букв: ', characters)


# 3 вариант
# with open('filess.txt', 'r', encoding='utf-8')  as file:
#     ennum = sum(1 for line in open('filess.txt', 'r'))
#     print(ennum)


