# Необходимо создать (не программно) текстовый файл, где каждая строка описывает
# учебный предмет и наличие  лекционных, практических и лабораторных занятий по
# этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
# были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран.

# 1 вариант
with open("dict.txt", "r", encoding='UTF-8') as file:
    my_dict = {}  # создаю множество
    for line in file:
        line_list = line.split(':')  # в списке разделяю данные по двоеточию
        num = ''
        num_list = []  # создаю список
        for i in line_list[1]:  # выбираю первый элемент - название
            if i.isdigit():  # проверяю все ли лементы в строке, начиная с 1 являются цифрами
                num = num + i  # прибаляю все цифры друг к другу
            else:
                if num != '':  # если не будет пробела, значит стоит число, следовательно добавляю элемент
                    num_list.append(int(num))
                    num = ''
        my_dict[line_list[0]] = sum(num_list)  # создаю множество с первым элементом и суммой часов
print(my_dict)

# 2 вариант (не совсем работает)
# with open("dict1.txt", "r") as file:
#     lines = file.read().splitlines()
#     my_dict = {}
# for line in lines:
#     key, value = line.split(': ')
#     my_dict.update({key: value})
# print(my_dict)

