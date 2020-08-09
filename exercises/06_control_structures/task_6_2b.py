# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
asking = True
while asking:
    try:
        flag = True
        ip_address = input('Enter IP-address in X.X.X.X format: ')
        ip_halfs = [int(s) for s in ip_address.split('.')]
        if len(ip_halfs) != 4 or ip_address.count('.') != 3:
            print('Incorrect format of IP-address.')
            flag = False
        else:
            for i in ip_halfs:
                if i > 255 or i < 0:
                    print('Incorrect numbers in IP-address.')
                    flag = False
                    break
        if flag:
            if ip_address == '255.255.255.255':
                print('local broadcast')
                asking = False
            elif ip_address == '0.0.0.0':
                print('unassigned')
                asking = False
            elif 0 < ip_halfs[0] < 224:
                print('unicast')
                asking = False
            elif 223 < ip_halfs[0] < 240:
                print('multicast')
                asking = False
            else:
                print('unused')
                asking = False 
    except ValueError:
        print('There cant be another symbols except of numbers and .')
