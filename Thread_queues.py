import queue
import threading
import time
class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False
class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables
        self.customers_threads = []
    def customer_arrival(self):
        for customer in range(1, 21):
            print(f'Посетитель номер {customer} прибыл')
            self.serve_customer(customer)
            time.sleep(1)
    def serve_customer(self, customer):
        free_table = False
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f'Посетитель номер {customer} сел за стол {table.number}')
                customer_thread = Customer(customer, self, self.queue, table)
                customer_thread.start()
                self.customers_threads.append(customer_thread)
                return
        if not free_table:
            print(f'Посетитель номер {customer} ожидает свободный стол')
            self.queue.put(customer)
class Customer(threading.Thread):
    def __init__(self, number, cafe, queue, table):
        super().__init__()
        self.number = number
        self.cafe = cafe
        self.queue = queue
        self.table = table
    def run(self):
        time.sleep(5)
        print(f'Посетитель номер {self.number} покушал и ушёл')
        self.table.is_busy = False
        if not self.queue.empty():
            next_customer = self.queue.get()
            self.cafe.serve_customer(next_customer)
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]
cafe = Cafe(tables)
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()
customer_arrival_thread.join()
for i in cafe.customers_threads:
    i.join()
