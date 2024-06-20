class Vehicle:
    __COLOR_VARIANTS = ['blue', 'green', 'yellow', 'black']
    def __init__(self, model, engine_power, color, owner):
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color
        self.owner = owner
    def get_model(self):
        return f'Модель: {self.__model}'
    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'
    def get_color(self):
        return f'Цвет: {self.__color}'
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')
    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    def __init__(self, model, engine_power, color, owner):
        super().__init__(model, engine_power, color, owner)
    def info(self):
        print(f'Количество мест: {self.__PASSENGERS_LIMIT}')
vehicle1 = Sedan('Toyota Mark II', 500, 'blue', 'Fedos')
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()
vehicle1.info()
