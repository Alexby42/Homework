class Vehicle:
    __COLOR_VARIANTS = ['blue', 'green', 'yellow', 'black']
    def __init__(self, __model, __engine_power, __color, owner):
        self.model = __model
        self.engine_power = __engine_power
        self.color = __color
        self.owner = owner
    def get_model(self):
        return f'Модель: {self.model}'
    def get_horsepower(self):
        return f'Мощность двигателя: {self.engine_power}'
    def get_color(self):
        return f'Цвет: {self.color}'
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')
    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            __color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')
class Sedan(Vehicle):
    def __init__(self, __model, __engine_power, __color, owner):
        super().__init__(__model, __engine_power, __color, owner)
        __PASSENGERS_LIMIT = 5
vehicle1 = Sedan('Toyota Mark II', 500, 'blue', 'Fedos')
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()