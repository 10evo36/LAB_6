#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: создайте словарь, связав его с переменной school , и наполните данными,
# которые бы отражали количество учащихся в разных классах (1а, 1б, 2б, 6а, 7в и т. п.).
# Внесите изменения в словарь согласно следующему: а) в одном из классов изменилось
# количество учащихся, б) в школе появился новый класс, с) в школе был расформирован
# (удален) другой класс. Вычислите общее количество учащихся в школе.
from datetime import date
import sys

if __name__ == '__main__':
    school = {'1a': 25, '1б': 23, '9a': 27, '9б': 22, '10a': 15,
              '10б': 12, '11a': 14, '11б': 11}
    print(school)

    school['9a'] += 1
    school['11в'] = 10
    school.pop('11a', 17)

    s = 0
    for item in school.values():
        s += item
    print(school)
    print("Количество учеников во всех классах", s)