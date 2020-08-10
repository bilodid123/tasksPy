# -*- coding: utf-8 -*-
"""
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
write_file = '/Users/arima/Documents/vsCodePy/tasksPy/exercises/07_files/config_sw1_cleared.txt'
ignore = ["duplex", "alias", "Current configuration"]
to_write = []
from sys import argv
file_name = argv[1]
with open(file_name, 'r') as f:
    for line in f:
      flag = True
      for i in ignore:
        if i in line:
          flag = False
      if not line.startswith('!') and flag:
          to_write.append(line.lstrip('\n'))
        #   print(line)
with open(write_file, 'w') as w:
    w.writelines(to_write)
