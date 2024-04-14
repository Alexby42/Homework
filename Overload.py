class Building:
    def __init__(self, str='one'):
        self.numberOfFloors = 1
        self.buildingType = str
    def __eq__(self, other):
        return self.numberOfFloors == self.buildingType
number_ = Building()
type_ = Building()
if number_ == type_:
    print('Целочисленное равно строковому параметру')
else:
    print('Целочисленное не равно строковому параметру')