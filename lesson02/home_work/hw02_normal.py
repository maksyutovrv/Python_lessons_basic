# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

print('***TASK 1***')

initial = [2, -5, 8, 9, -25, 25, 4]
new = []

print('ДАНО: ', initial)
for element in initial:
    print(type(element**.5))
    if type(element**.5) is float and int(element**.5) == element**.5:
        new.append(int(element**.5))
print('РЕШЕНИЕ: ', new)


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

print('***TASK 2***')

date = '02.11.2013'
day = int(date[0:2])
month = int(date[3:5])
year = int(date[6:10])
print(day, month, year)

titles = {
    'days':
        {1: 'первое', 2: 'второе', 3: 'третье', 4: 'четвертое', 5: 'пятое', 6: 'шестое', 7: 'седьмое', 8: 'восьмое',
         9: 'девятое', },
    'months':
        {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа',
         9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'}
}
print(titles['days'][day], titles['months'][month], year, 'года')




# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

print('***TASK 3***')

import random

print('Введите размер списка: ')
n = int(input())
i = 0
list_1 = []

while i < n:
    i = i + 1
    list_1.append(random.randint(0, 200) - 100)

print(list_1)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

print('***TASK 4***')

lst = [1, 2, 4, 5, 6, 2, 5, 2]
lst2 = list(set(lst))
print(lst2)

lst_3 = []
i = 0

for element in lst:
    i = i + 1
    if (element not in lst[i:]) and (element not in lst[:i-1]):
        lst_3.append(element)

print(lst_3)