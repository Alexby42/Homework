class House:
    def __init__(self):
        self.numberOfFloors = 10
house = House()
for i in range(house.numberOfFloors):
    print('Текущий этаж равен:', i + 1)
