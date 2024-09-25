print('Задача 7. Пирамидка 2')

# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
#
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

height = int(input('Введите количество уровней пирамиды: '))
current_number = 1
for row in range(1, height + 1):
    spaces = ' ' * (height - row) * 2
    numbers = ''
    for _ in range(row):
        numbers += f'{current_number:<4}'
        current_number += 2
    print(spaces + numbers)
