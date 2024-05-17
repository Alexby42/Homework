class InvalidDataException(Exception):
    def __init__(self, message, info):
        self.message = message
        self.info = info
class ProcessingException(Exception):
    def __init__(self, message):
        self.message = message
def func(value):
    if value < 0:
        raise InvalidDataException('Некорректные данные', 'Данные должны быть положительным числом')
    if value == 0:
        raise ProcessingException('Данные должны быть больше нуля')
    return value
try:
    user_input = input('Введите число:')
    value = int(user_input)
    func(value)
except InvalidDataException as exc:
    print('Допущена ошибка ввода')
    print(f'Сообщение об ошибке: {exc.message}')
    print(f'Дополнительная информация: {exc.info}')
    raise
except ProcessingException as exc:
    print('Допущена ошибка ввода')
    print(f'Сообщение об ошибке: {exc.message}')
except ValueError:
    print('Введено некорректное значение. Введите число!')
else:
    print('Поздравляю! Вы ввели числовое значение!')
finally:
    print('Программа завершила работу')