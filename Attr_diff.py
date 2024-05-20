class Building:
    total = 0
    def __init__(self):
        Building.total += 1
        print(Building.total)
list_ = []
building_total = 40
while len(list_) < building_total:
    building = Building()
    list_.append(building)
