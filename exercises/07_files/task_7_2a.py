# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]
from sys import argv
file_name = argv[1]
with open(file_name, 'r') as f:
    for line in f:
      flag = True
      for i in ignore:
        if i in line:
          flag = False
      if not line.startswith('!') and flag:
        print(line.strip())
