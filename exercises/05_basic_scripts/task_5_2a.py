# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28  в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ip_address = input('Enter IP in format Network/Mask: ')
# split mask and network and save them into ints
network = ip_address.split('/')[0]
mask = ip_address.split('/')[1]
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
