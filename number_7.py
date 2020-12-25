import json

with open("firm.txt", "r", encoding='UTF-8') as file:
    firm_profit = {}
    firm_losses = {}
    profit_fin = 0
    for column in file:
        column_list = column.split() # делаю разделение по пробелам в строках
        revenues = int(column_list[2])  # перевожу 3 столбец в цифры
        costs = int(column_list[3])  # перевожу 4 столбец в цифры
        if revenues >= costs:  # если 3 столбец больше 4, то получаем профит
            profit = revenues - costs
            firm_profit[column_list[0]] = profit  # добавляю в множество первый столбец
        else:
            losses = costs - revenues
            firm_losses[column_list[0]] = losses

    firm_average = {"average_profit": firm_profit}  # Смотрю какие фирмы
    firm = [firm_profit, firm_average]  # вывод в множестве фирмы с прибылью
    if len(firm_losses) != 0:
        firm.append(firm_losses)  # выводит фирмы с убытком

with open("firm.json", "w", encoding='UTF-8') as j_file:
    json.dump(firm, j_file)  # запись файла в json

print(firm)