# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
zxc = ospf_route.split(', ')
first_three = zxc[0].split()
last_two = zxc[1:]
phrases = ['Prefix','AD/Metric','Next-Hop','Last update','Outbound Interface']
print(f'{phrases[0]:22}{first_three[0]}')
print(f'{phrases[1]:22}{first_three[1]}')
print(f'{phrases[2]:22}{first_three[3]}')
print(f'{phrases[3]:22}{last_two[0]}')
print(f'{phrases[4]:22}{last_two[1]}')