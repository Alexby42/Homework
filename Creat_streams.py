from time import sleep
from threading import Thread
def num():
    for i in range(1, 11):
        print(i)
        sleep(1)
def word():
    for j in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']:
        print(j)
        sleep(1)
thread1 = Thread(target=num)
thread2 = Thread(target=word)
thread1.start()
thread2.start()
thread1.join()
thread2.join()