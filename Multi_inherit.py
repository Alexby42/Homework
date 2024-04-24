class Vehicle:
    vehicle_type = 'None'
class Car:
    price = 1000000
    def Horse_powers(self, hp):
        self.hp = hp
        print('Кол-во лошадиных сил:', self.hp)
class Nissan(Car, Vehicle):
    price = 2000000
    vehicle_type = 'Автомобиль'
auto = Nissan()
print(auto.vehicle_type)
print('Стоимость:',auto.price)
auto.Horse_powers(100)