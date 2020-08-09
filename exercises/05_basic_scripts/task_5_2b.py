# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv
network = argv[1]
mask = argv[2]

# split mask and network and save them into ints
net_ints = [int(s) for s in network.split('.')]
mask_int = int(mask)
# network calculations
ip_string = ''
for s in net_ints:
    ip_string += f'{s:08b}'
new_string = ip_string[:mask_int] + (32 - mask_int) * '0'
new_net = [new_string[i:i+8] for i in range(0,len(new_string), 8)]
# mask calculations
ones, zeros = mask_int, 32 - mask_int
mask_str = '1' * ones + '0' * zeros
mask_numbers = [mask_str[i:i+8] for i in range(0, len(mask_str),8)]
msknums = mask_numbers
# formated printing
print('\nNetwork:')
print(f'{int(new_net[0],2):<8} {int(new_net[1],2):<8} {int(new_net[2],2):<8} {int(new_net[3],2):<8}')
print(f'{new_net[0]} {new_net[1]} {new_net[2]} {new_net[3]}')
print('\nMask:')
print(f'{int(msknums[0],2):<8} {int(msknums[1],2):<8} {int(msknums[2],2):<8} {int(msknums[3],2):<8}')
print(f'{msknums[0]} {msknums[1]} {msknums[2]} {msknums[3]}')