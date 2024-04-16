class House:
    def __init__(self):
        self.numberOfFloors = 10
        for i in range(self.numberOfFloors):
            print('Текущий этаж равен:', i + 1)
house = House()
