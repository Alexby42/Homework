class Building:
    def __init__(self, str=None):
        self.numberOfFloors = 0
        self.buildingType = str
    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType
number1 = Building(7)
number2 = Building(7)
type1 = Building('seven')
type2 = Building('twenty four')
print(number1 == number2)
print(type1 == type2)
