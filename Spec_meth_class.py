class House:
    def __init__(self):
        self.numberOfFloors = 0
    def setNewNumberOfFloors(self):
        self.numberOfFloors = 5
house = House()
house.setNewNumberOfFloors()
print(house.numberOfFloors)
