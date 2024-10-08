import math

print('Задача 5. Вот это объёмы!')

# Для курсовой работы по физике
# Андрею нужно сравнить объёмы двух планет: Земли и какой-нибудь случайной,
# которая может в теории существовать в нашей вселенной.
# Андрей хорошо разбирается в формулах,
# а вот считать что-то, а уж тем более самому - это явно не его.
# Объём Земли ему известен заранее  - это 10.8321 * 10 ** 11 км3
#
# А вот объём случайной планеты ему нужно будет посчитать.
# Благо, у него есть формула
#
# V = 4/3 πR ** 3
#
# где V - это объём, π - число пи, а R - радиус планеты.
#
# Напишите программу,
# которая получает на вход радиус случайной планеты
# и выводит на экран во сколько раз планета Земля меньше или больше по объёму.
# Ответ округлите до трёх знаков после запятой

# Пример:
# Введите радиус случайной планеты: 3389.5
# Объём планеты Земля больше в 6.641 раз

# Пример 2:
# Введите радиус случайной планеты: 7000
# Объём планеты Земля меньше в (1/0.754) = 1.326 раз

radius_planet = float(input('Введите радиус случайной планеты: '))
volume_earth = 10.8321 * 10 ** 11
volume_planet = 4 / 3 * math.pi * radius_planet ** 3
result = round(volume_earth / volume_planet, 3)
if volume_earth > volume_planet:
    print(f'Объём планеты Земля больше в {result} раз')
else:
    less_earth = round(1/result, 3)
    print(f'Объём планеты Земля меньше в (1/{result}) = {less_earth} раз')
