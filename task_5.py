print('Задача 5. Наибольшая сумма цифр')

# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

total_numbers = int(input('Введите количество чисел: '))
max_sum = 0
max_number = 0
for _ in range(total_numbers):
    number = int(input('Введите число: '))
    temp_number = number
    digit_sum = 0
    while temp_number > 0:
        digit_sum += temp_number % 10
        temp_number //= 10

    if digit_sum > max_sum:
        max_sum = digit_sum
        max_number = number
print(f'Число с наибольшей суммой цифр: {max_number}, сумма его цифр: {max_sum}')