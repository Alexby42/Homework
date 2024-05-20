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
