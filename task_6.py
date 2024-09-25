print('Задача 6. Ход конём')

# В рамках разработки шахматного ИИ стоит новая задача.
# По заданным вещественным координатам коня
# и второй точки программа должна определить может ли конь ходить в эту точку.
#
# Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.

# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.

x_horse, y_horse = -1.0, -1.0
x_point, y_point = -1.0, -1.0

while x_horse < 0 or x_horse > 7.0 or y_horse < 0 or y_horse > 7.0:
    print('Введите местоположение коня:')
    x_horse = float(input())
    y_horse = float(input())

while x_point < 0 or x_point > 7.0 or y_point < 0 or y_point > 7.0:
    print('Введите местоположение точки на доске:')
    x_point = float(input())
    y_point = float(input())

x_horse_square = int(x_horse * 10)
y_horse_square = int(y_horse * 10)
x_point_square = int(x_point * 10)
y_point_square = int(y_point * 10)

print(f'Конь в клетке ({x_horse_square}, {y_horse_square}). Точка в клетке ({x_point_square}, {y_point_square})')

dx = abs(x_point_square - x_horse_square)
dy = abs(y_point_square - y_horse_square)

if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
    print("Да, конь может ходить в эту точку.")
else:
    print("Нет, конь не может ходить в эту точку.")
