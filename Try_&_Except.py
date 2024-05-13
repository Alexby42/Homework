def add_everything_up(a, b):
    try:
        print(a + b)
    except TypeError as exc:
        print('Ошибка: неподдерживаемые типы операндов для суммирования', exc)
    else:
        print('А что, так можно было?')
    finally:
        return f'123.456строка'
print(add_everything_up(123.456, 'строка'))
print()
def add_everything_up(a, b):
    try:
        print(a + b)
    except TypeError:
        print('Нельзя суммировать разные типы данных, но...')
    finally:
        return f'яблоко4215'
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