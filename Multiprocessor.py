import multiprocessing
class WarehouseManager:
    data = {}
    def process_request(self, request):
        self.request = request
        for key, arg_, value in requests:
            if arg_ == 'receipt':
                self.data.setdefault(key, value)
                if arg_ == 'shipment':
                    self.data[value] -= [value]
        return self.data
    def run(self):
        for request in self.data:
            request.start()
                


manager = WarehouseManager()

requests = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50)
]

manager.run()

print(manager.data)