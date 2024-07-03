import multiprocessing
def process_request(queue, data):
    while True:
        request = queue.get()
        if request is None:
            break
        key, arg_, value = request
        if arg_ == 'receipt':
            if key in data:
                data[key] += value
            else:
                data[key] = value
        elif arg_ == 'shipment':
            if key in data and data[key] >= value:
                data[key] -= value
class WarehouseManager:
    def __init__(self):
        self.manager = multiprocessing.Manager()
        self.data = self.manager.dict()
        self.queue = multiprocessing.Queue()
    def run(self, requests):
        worker_process = multiprocessing.Process(target=process_request, args=(self.queue, self.data))
        worker_process.start()
        for request in requests:
            self.queue.put(request)
        self.queue.put(None)
        worker_process.join()

if __name__ == '__main__':
    manager = WarehouseManager()
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]
    manager.run(requests)
    print(manager.data)