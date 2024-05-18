def add_everything_up(a, b):
    try:
        print(a + b)
    except TypeError as exc:
        print('Ошибка: неподдерживаемые типы операндов для суммирования', exc)
        print(str(a) + b)
    finally:
        return f'Но задача решена'
print(add_everything_up(123.456, 'строка'))
print()
def add_everything_up(a, b):
    try:
        print(a + b)
    except TypeError:
        print('Нельзя суммировать разные типы данных')
        print(a + str(b))
    finally:
        return f'Но задача решена'
print(add_everything_up('яблоко', 4215))
print()
def add_everything_up(a, b):
    try:
        print(a + b)
    except:
        print('А целые числа суммировать можно?')
    else:
        print('Оказывается, целые числа суммируются!')
    finally:
        return f'Кажется все прошло удачно'
print(add_everything_up(123.456, 7))
