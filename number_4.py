# Создать (не программно) текстовый файл со следующим содержимым:
#
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

# 1 вариант
my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open(r"one_two_three_four.txt", 'a') as translate:
    with open(r"one_two_three_four.txt") as translating:
        for line in translating:
            new_line = line.split(" - ")
            new_line[0] = my_dict.get(new_line[0])
            translate.writelines(new_line[0] + ' - ' + new_line[1])

# 2 вариант
# from translate import Translator
# with open('one_two_three_four.txt', 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)
#     translator = Translator(from_lang="English", to_lang="Russian")
#     # В целом можно было не использовать блок translate, а просто задать определенные имена каждому слову и все
#     # но это на будущее для улучшения программы
#     word1 = translator.translate('One')
#     word2 = translator.translate('Two')
#     word3 = translator.translate('Three')
#     word4 = translator.translate('Four')
#     with open('one_two_three_four.txt', 'w', encoding='utf-8') as files:
#         # это тупо, если слов будет больше - код будет гигантский, на каникулах подумаю как доработать
#         contents = files.write(word1 + ' - 1' + '\n' + word2 + ' - 2' + '\n' + word3 + ' - 3' + '\n' + word4 + ' - 4')

# 3 вариант (не совсем так работает, сложновато работать с файлами)
# with open('one_two_three_four.txt', 'a', encoding='utf-8') as file:
#     # Если открыть файл просто на чтение, то он будет выдавать ошибку IO, не смог разобраться в этом
#     content = file.read()
#     print(content)
#
#     with open('one_two_three_four.txt', 'w', encoding='utf-8') as files:
#         k = 0
#         while k < 4:
#             new_string = input('Введите текст цифры и саму цифру через тире: ')
#             contents = file.write(new_string + '\n')
#             k += 1
#             print(contents)

# 4 вариант
# with open('one_two_three_four.txt', 'a', encoding='utf-8') as file:
#     content = file.read()
#     print(content)
#     k = 0
#     while k < 4:
#         new_string = input('Введите текст цифры и саму цифру через тире: ')
#         contents = file.write('\n' + new_string + '\n')
#         k += 1
#         print(contents)
