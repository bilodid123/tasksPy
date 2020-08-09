# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

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
      elif ip_address == '0.0.0.0':
         print('unassigned')
      elif 0 < ip_halfs[0] < 224:
         print('unicast')
      elif 223 < ip_halfs[0] < 240:
         print('multicast')
      else:
         print('unused') 
except ValueError:
   print('There cant be another symbols except of numbers and .')
