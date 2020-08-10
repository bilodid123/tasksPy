# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
vlan = input('Enter the VLAN number: ')
with open('/Users/arima/Documents/vsCodePy/tasksPy/exercises/07_files/CAM_table.txt', 'r') as read_file:
    for line in read_file:
       if vlan in line.strip('\n').split():
           print(line.strip())