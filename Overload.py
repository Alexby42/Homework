class Building:
    def __init__(self, floors, type_):
        self.type_ = type_
        self.floors = floors
    def __eq__(self, other):
        return self.floors == other.floors and self.type_ == other.type_
building1 = Building(10, 'ten')
building2 = Building(10, 'ten')
print(building1 == building2)
