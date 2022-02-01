# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

out_f = open("file_1.txt", "w")
while True:
    input_string = input('Введите построчно данные. Для окончания введите пустую строку: ')
    if input_string == '':
        break
    out_f.write(f'{input_string}\n')
out_f.close()


# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

with open('file_2.txt') as f_obj:
    content = f_obj.readlines()
    print(f'В файле {len(content)} строк')
    for num, line in enumerate(content, 1):
        print(f'В строке {num} : {line.count(" ") + 1} слов(а)')


# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

total_salary = 0

with open('file_3.txt', encoding='utf-8') as file:
    content = file.readlines()
    for line in content:
        surname, salary = line.rstrip('\n').split(' ')
        salary = float(salary)
        total_salary += salary
        if salary < 20000:
            print(f'{surname}')
    print(f'Средний доход сотрудников = {round(total_salary / len(content), 2)}')

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

translate_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('file_4.txt', encoding='utf-8') as file_r, open('file_4_out.txt', 'w', encoding='utf-8') as file_w:
    for line in file_r.readlines():
        text_number, number = line.rstrip().split(' — ')
        file_w.write(f'{translate_dict[text_number]} — {number}\n')

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

import random

# Очищаем файл перед записью нового набора чисел
with open('file_5.txt', 'w') as file:
    file.write('')
# Записываем 100 случайных чисел
with open('file_5.txt', 'a') as file:
    for i in range(100):
        file.write(f'{random.randint(0, 10)} ')
# Считаем сумму
with open('file_5.txt', 'r') as file:
    print(f'Сумма чисел в файле = {sum([int(i) for i in file.read().split() if i.isdigit()])}')


# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие
# лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. Необязательно,
# чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

result_dict = {}
with open('file_6.txt', encoding='utf-8') as file:
    for line in file:
        lesson_type, *lessons = line.split()
        lesson_count = [int(lesson.rstrip('(л)(пр)(лаб)')) for lesson in lessons if lesson != '—']
        result_dict.update({lesson_type.rstrip(":"): sum(lesson_count)})

print(result_dict)

# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

result_list = []
dict_plus_prosfit = {}
dict_minus_profit = {}
with open('file_7.txt') as file:
    average_profit_list = []
    for line in file.readlines():
        name, _, revenue, costs = line.rstrip().split()
        profit = int(revenue) - int(costs)
        if profit > 0:
            average_profit_list.append(profit)
            dict_plus_prosfit.update({name: profit})
        else:
            dict_minus_profit.update({name: profit})
    result_list.append(dict_plus_prosfit)
    result_list.append(dict_minus_profit)
    result_list.append({'average_profit': sum(average_profit_list) / len(average_profit_list)})

with open('file_7.json', 'w') as file:
    json.dump(result_list, file)