def create_operation(n):
    if n == 1:
        def div(x, y):
            return x / y
        return div
    elif n == 2:
        def mult(x, y):
            return x * y
        return mult
print('Задача 1: Фабрика функций')
my_func_div = create_operation(1)
print('Функция деления - ', my_func_div(6,4))
my_func_mult = create_operation(2)
print('Функция умножения - ', my_func_mult(8,2))
print()
square = lambda x: x ** 2
print('Задача 2: Лямбда')
print('Квадрат числа - ', square(10))
def square_def(x):
    return x ** 2
print('Квадрат числа через def - ', square_def(10))
print()
class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __call__(self):
        return self.a * self.b
area_rect = Rect(7, 9)
print('Задача 3: Вызываемые oбъекты')
print('Стороны прямоугольника:', vars(area_rect))
print('Площадь:', area_rect())