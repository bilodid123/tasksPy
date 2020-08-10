# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

data = []
with open('/Users/arima/Documents/vsCodePy/tasksPy/exercises/07_files/ospf.txt', 'r') as f:
    strings = f.readlines()
print(strings)
print('\n')
for string in strings:
    string.rstrip()
    info = string.split()
    data.append(info[1:])
show = ['Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface'] 
for i in range(len(data)):
    print('\n')
    print(f'{show[0]:<20} {data[i][0]}')
    print(f'{show[1]:<20} {data[i][1][1:-1]}')
    print(f'{show[2]:<20} {data[i][3][:-1]}')
    print(f'{show[3]:<20} {data[i][4][:-1]}')
    print(f'{show[4]:<20} {data[i][5]}')
    print('\n')
