from datetime import datetime
class SuperDate(datetime):
    list_season = {(12, 1, 2): 'Winter', (3, 4, 5): 'Spring', (6, 7, 8): 'Summer', (9, 10, 11): 'Autumn'}
    dict_time = {range(6, 12): 'Morning', range(12, 18): 'Day', range(18, 24): 'Evening', range(0, 6): 'Night'}
    def __init__(self, year, month, day, hour):
        self.date = datetime(year, month, day, hour)
    def get_season(self):
        for current in self.list_season:
            if self.date.month in current:
                return self.list_season[current]
    def get_time_of_day(self):
        for current in self.dict_time:
            if self.date.hour in current:
                return self.dict_time[current]
data = SuperDate(2024, 2, 22, 12)
print(data.get_season())
print(data.get_time_of_day())