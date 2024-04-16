class Building:
    def __init__(self, floors, type_):
        self.numberOfFloors = floors
        self.buildingType = type_
    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType
building1 = Building(10, 'ten')
building2 = Building(10, 'ten')
print(building1 == building2)
