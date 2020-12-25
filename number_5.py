# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
# выводить ее на экран.

with open('summ.txt', 'w', encoding='utf-8') as file:
    content = list(input('Введите числа через пробел: ').split())  # создаю список с элементами через пробел
    for line in content:  # все элементы списка на новой строчке
        file.write(line + '\n')
with open('summ.txt', 'r', encoding='utf-8') as files:
    readd = files.readlines()
    str_readd = str(readd)
    # q = 0
    num = 0
    for line in readd:  # делаю отбор по элементам списка
        try:
            num += int(line)  # тут отбираюся и суммируются только цифры из списка, если не цифра будет ошибка, обработанная ниже
            # q += num
        except ValueError:
            print('Тут есть не цифра, но я суммирую только цифры')
    print(f'Сумма чисел: {num}')
        # result = sum(map(int, files))
        # print(f'Сумма чисел: {result}')
