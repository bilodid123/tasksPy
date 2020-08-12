# -*- coding: utf-8 -*-
"""
Задание 9.1a

Сделать копию функции generate_access_config из задания 9.1.

Дополнить скрипт:
* ввести дополнительный параметр, который контролирует будет ли настроен port-security
 * имя параметра 'psecurity'
 * значение по умолчанию None
 * для настройки port-security, как значение надо передать список команд port-security (находятся в списке port_security_template)

Функция должна возвращать список всех портов в режиме access
с конфигурацией на основе шаблона access_mode_template и шаблона port_security_template, если он был передан.
В конце строк в списке не должно быть символа перевода строки.


Проверить работу функции на примере словаря access_config,
с генерацией конфигурации port-security и без.

Пример вызова функции:
print(generate_access_config(access_mode_template, access_config))
print(generate_access_config(access_mode_template, access_config, port_security_template))

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security",
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}

def generate_access_config(intf_vlan_mapping, access_template, psecurity = None):
    info = []
    for key in intf_vlan_mapping:
        if psecurity == None:
            info.append(f'interface {key}')
            for line in access_template:
                if line.endswith('access vlan'):
                    info.append(f'{line} {intf_vlan_mapping[key]}')
                else:
                    info.append(line)   
        else:
            info.append(f'interface {key}')
            for line in access_template:
                if line.endswith('access vlan'):
                    info.append(f'{line} {intf_vlan_mapping[key]}')
                else:
                    info.append(line)
            for switch in psecurity:
                    info.append(switch)
    return info