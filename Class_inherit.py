class Car:
    price = 1000000
    def __str__(self):
        return 'Автомобиль {}, Стоимость: {}'.format(self.__class__.__name__, self.price)
    def Horse_powers(self, hp):
        self.hp = hp
        print('Кол-во лошадиных сил:', self.hp)
class Nissan(Car):
    price = 2000000
class Kia(Car):
    price = 3000000
auto1 = Car()
print(auto1)
auto1.Horse_powers(200)
auto2 = Nissan()
print(auto2)
auto2.Horse_powers(300)
auto3 = Kia()
print(auto3)
auto3.Horse_powers(400)

print('--------------------Первый вариант, получившийся на основе лекций--------------------')

class Car:
    price = 1000000
    def __init__(self, Horse_powers):
        self.Horse_powers = Horse_powers
    def __str__(self):
        return 'Автомобиль {}, Стоимость: {}, Кол-во лошадиных сил: {}'.format(
            self.__class__.__name__, self.price, self.Horse_powers)
class Nissan(Car):
    price = 2000000
class Kia(Car):
    price = 3000000
auto1 = Car(200)
print(auto1)
auto2 = Nissan(300)
print(auto2)
auto3 = Kia(400)
print(auto3)
