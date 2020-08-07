# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_address = input('Enter IP in format Network/Mask: ')
network = ip_address.split('/')[0]
mask = ip_address.split('/')[1]
net_ints = [int(s) for s in network.split('.')]
mask_int = int(mask)
print('\nNetwork:')
print(f'{net_ints[0]:<8} {net_ints[1]:<8} {net_ints[2]:<8} {net_ints[3]:<8}')
print(f'{net_ints[0]:08b} {net_ints[1]:08b} {net_ints[2]:08b} {net_ints[3]:08b}')
print('\nMask:')
ones,zeros = mask_int // 8, (32 - mask_int) // 8

# twohun = '255      '
# zero   = '0        '
# ones_str = '11111111 '
# zeros_str = '00000000 '
# print(twohun * ones + zero * zeros)
# print(ones_str * ones + zeros_str * zeros)

print(f'{255:<8} ' * ones + f'{0:<8} ' * zeros)
print(f'{255:<08b} ' * ones + f'{0:08b} ' * zeros)




