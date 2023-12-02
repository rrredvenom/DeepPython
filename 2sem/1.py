# Проверить типы разных переменных

# a = 458
# b = 'Python'
# c = 25* 2 / 36
# d = False
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))


# Создайте в переменной data список значений разных
# типов перечислив их через запятую внутри квадратных скобок.
# Для каждого элемента в цикле выведите:
# порядковый номер начиная с единицы
# значение
# адрес в памяти
# размер в памяти
# хэш объекта
# результат проверки на целое число только если он положительный
# результат проверки на строку только если он положительный
#
# *Добавьте в список повторяющиеся элементы и сравните на результаты.

# import sys
# data = [54, "test_str", 2.158, True, 54]

# for idx, elem in enumerate(data, 1):
#     print(idx, elem, id(elem), sys.getsizeof(elem), hash(elem))
#     # print(elem)
#     # print(id(elem))
#     # print(sys.getsizeof(elem))
#     # print(hash(elem))
#     if isinstance(elem, int):
#         print('Целое число')
#     if isinstance(elem, str):
#         print('Строка')

# Напишите программу, которая получает целое число
# и возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.

# *Дополнительно
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно

# number = int(input())
# print(bin(number))
# print(oct(number))

# for i in [2, 8]:
#     n = number
#     res = ''
#     while n:
#         res = f'{n % i}' + res
#         n //= i
#     print(res)

# Напишите программу, которая вычисляет площадь круга и
# длину окружности по введённому диаметру.
# Диаметр не превышает 1000 у.е.
# Точность вычислений должна составлять
# не менее 42 знаков после запятой.

# import math
# import decimal

# decimal.getcontext().prec = 42

# def circle_diameter(dim):
#     return decimal.Decimal(math.pi) * pow((dim/2),2)

# def circumference (diameter):
#     return decimal.Decimal(math.pi) * diameter

# diameter = decimal.Decimal(input(f"не более тысячи :"))

# print(circle_diameter(diameter))
# print(circumference(diameter))

# Напишите программу, которая решает квадратные уравнения
# даже если дискриминант отрицательный.
# Используйте комплексные числа для извлечения квадратного корня.

# import math

# def diskriminant(a, b, c):
#     return pow(b, 2) - 4 * a *c



# a = float(input("Введите а: "))
# b = float(input("Введите b: "))
# c = float(input("Введите c: "))

# # print(diskriminant(a, b ,c))

# dis = diskriminant(a, b, c)
# kor_dis = pow(diskriminant(a, b, c), 0.5)

# if dis > 0:
#     print((-b + kor_dis) / (2 * a))
#     print((-b - kor_dis) / (2 * a))
# elif dis == 0:
#     print((-b - kor_dis) / (2 * a))
# else:
#     print((-b + kor_dis) / (2 * a))
#     print((-b - kor_dis) / (2 * a))

# # print(pow(diskriminant(a, b, c), 0.5))

