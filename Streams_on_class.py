from time import sleep
from threading import Thread
class Knight(Thread):
    def __init__(self, name, skill):
        super().__init__()
        self.name = name
        self.skill = skill
    def run(self):
        warrior = 100
        print(f'{self.name}, на нас напали!')
        for days in range(1, 20):
            warrior -= self.skill
            if warrior >= 0:
                sleep(1)
                print(f' {self.name}, сражается {days} день(дня)..., осталось {warrior} воинов')
            else:
                print(f'{self.name} одержал победу спустя {days-1} дней!')
                break
knight1 = Knight('Sir Lancelot', 10)
knight2 = Knight('Sir Galahad', 20)
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print('Все битвы закончились!')